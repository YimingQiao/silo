#pragma once

#include "../util.h"
#include "../third-party/libraman/bit_stream.h"
#include "../third-party/libraman/canonical_code.h"
#include "../third-party/libraman/code_tree.h"
#include "../third-party/libraman/frequency_table.h"
#include "../third-party/libraman/coder.h"
#include "tpcc.h"
#include "../record/encoder.h"
#include "raman_dummy.h"
#include "abstract_ordered_index.h"
#include "disk_storage.h"

using vector_of_string = std::vector<std::string>;

// -------------------------------- Raman Table  -------------------------------------
template<typename T>
class RamanTable {
public:
    RamanTable() : sample_size_(sizeof(T)) {};

    inline ALWAYS_INLINE void PushTuple(const T &tuple) { table_.push_back(std::move(ToRamanFormat(tuple))); }

    inline ALWAYS_INLINE vector_of_string &GetTuple(size_t index) { return table_[index]; }

    inline ALWAYS_INLINE void Clear() { table_.clear(); }

    std::vector <vector_of_string> table_;
    size_t sample_size_;
};

// ------------------------------- Raman Compressor ----------------------------------
class RamanCompressor {
public:
    RamanCompressor() = default;

    explicit RamanCompressor(size_t num_fields) : stats_(num_fields) {}

    std::vector <raman::FreqStat> stats_;
    std::vector <raman::CodeTree> forest_;

public:
    // ------------------------- API for Raman Compression -------------------------
    void RamanLearning(std::vector <std::vector<std::string>> &samples);

    inline ALWAYS_INLINE std::string RamanCompress(vector_of_string &raman_sample) {
        std::string result;
        unsigned char currentByte = 0;
        int bitsFilled = 0;
        for (size_t i = 0; i < raman_sample.size(); ++i) {
            size_t sym = stats_[i].Str2Idx(raman_sample[i]);
            std::vector<bool> code = forest_[i].GetCode(sym);

            for (bool bit: code) {
                currentByte = (currentByte << 1) | bit;
                bitsFilled++;

                if (bitsFilled == 8) {
                    result.push_back(static_cast<char>(currentByte));
                    currentByte = 0;
                    bitsFilled = 0;
                }
            }
        }

        // Handle any remaining bits
        if (bitsFilled > 0) {
            currentByte <<= (8 - bitsFilled); // Shift remaining bits to the left
            result.push_back(static_cast<char>(currentByte));
        }

        return result;
    }

    template<typename T>
    inline ALWAYS_INLINE std::string RamanCompress(const T &sample) {
        std::vector <std::string> raman_sample = ToRamanFormat(sample);
        return RamanCompress(raman_sample);
    }

    template<typename T>
    inline ALWAYS_INLINE void RamanDecompress(const std::string &bit_string, T &sample) {
        size_t sym;
        uint32_t bitPos = 0;  // To track the position in bits
        size_t num_fields = stats_.size();
        std::vector <std::string> raman_sample(num_fields);

        auto getBit = [&bit_string, &bitPos]() -> bool {
            bool bit = (bit_string[bitPos / 8] >> (7 - (bitPos % 8))) & 1;
            bitPos++;
            return bit;
        };

        for (size_t i = 0; i < num_fields; ++i) {
            // You will need to modify the Decode function to accept the getBit lambda or
            // change its implementation to read bits using the lambda.
            raman::Decode(sym, &forest_[i], getBit);
            raman_sample[i] = stats_[i].Idx2Str(sym);
        }

        FromRamanFormat(raman_sample, sample);
    }

    RamanCompressor *Copy() {
        RamanCompressor *ret = new RamanCompressor();
        ret->stats_ = stats_;
        for (auto &stat: ret->stats_) {
            raman::CodeTree tree = stat.BuildCodeTree();
            raman::CanonicalCode code(tree, stat.getSymbolLimit());
            ret->forest_.push_back(code.toCodeTree());
        }
        return ret;
    }

    uint32_t Size() {
        uint32_t ret = 0;
        for (auto &stat: stats_) ret += stat.BimapSize();
        for (auto &tree: forest_) ret += tree.Size();
        return ret;
    }

private:
    void SetNumFields(size_t num_fields) { stats_.resize(num_fields); }
};

// -------------------------------- Raman Tuple Block -------------------------------------\

template<typename T>
class RamanTupleBlock {
public:
    const size_t kBufferSize = 1024 * 8;

public:
    const int32_t id;
    int32_t n_tuple;
    std::vector<typename T::key> keys_;

    RamanTupleBlock(int32_t worker_id) : n_tuple(0), values_(kBufferSize), keys_(kBufferSize), id(worker_id) {}

public:
    using key = typename T::key;
    using value = typename T::value;

    inline ALWAYS_INLINE bool Insert(const key &key, const value &value) {
        keys_[n_tuple] = key;
        values_[n_tuple] = value;
        return ++n_tuple == kBufferSize;
    }

    uint64_t BlockCompress(vector_of_string &compressed_values, uint64_t &dict_id) {
        // block learning
        std::vector <std::vector<std::string>> samples;
        for (auto &sample: values_) samples.push_back(ToRamanFormat(sample));
        RamanCompressor *cpr = new RamanCompressor();
        cpr->RamanLearning(samples);
        compressors_.push_back(cpr);

        // block compress
        for (auto &sample: samples) compressed_values.push_back(cpr->RamanCompress(sample));

        // set dict id
        dict_id = compressors_.size() - 1;

        return cpr->Size();
    }

    inline ALWAYS_INLINE void Decompress(Tuple<std::string> &tuple, value &sample) {
        if (tuple.is_cprd_) {
            RamanCompressor *cpr = GetCompressor(tuple.id_dict_);
            cpr->RamanDecompress(tuple.data_, sample);
        } else {
            Decode(tuple.data_, sample);
            if (CprNum() > tuple.id_dict_ && tuple.id_thread_ == id) {
                RamanCompressor *cpr = GetCompressor(tuple.id_dict_);
                std::string codes = cpr->RamanCompress(sample);
                cpr->RamanDecompress(codes, sample);
            }
        }
        return;
    }

    inline ALWAYS_INLINE value &GetValue(key &key) {
        for (int32_t i = 0; i < n_tuple; ++i) { if (keys_[i] == key) return &values_[i]; }
        return nullptr;
    }

    inline ALWAYS_INLINE void AddCompressor(RamanCompressor *compressor) { compressors_.push_back(compressor); }

    inline ALWAYS_INLINE uint32_t Size() {
        uint32_t raman_dict_size = 0;
        for (auto *compressor: compressors_) raman_dict_size += compressor->Size();
        return raman_dict_size;
    }

    inline ALWAYS_INLINE uint32_t CprNum() { return compressors_.size(); }

private:
    std::vector<typename T::value> values_;
    std::vector<RamanCompressor *> compressors_;

    inline ALWAYS_INLINE RamanCompressor *GetCompressor(int32_t dict_id) {
        if (dict_id < 0 || dict_id >= compressors_.size())
            throw std::runtime_error("Invalid dict id in GetCompressor");
        return compressors_[dict_id];
    }
};