#pragma once

#include "../util.h"
#include "../third-party/libraman/bit_stream.h"
#include "../third-party/libraman/canonical_code.h"
#include "../third-party/libraman/code_tree.h"
#include "../third-party/libraman/frequency_table.h"
#include "../third-party/libraman/coder.h"
#include "tpcc.h"
#include "../record/encoder.h"

using vector_of_string = std::vector<std::string>;

static tuple_cpr::value Tuple(std::string &data, size_t dict_id = 0) {
    tuple_cpr::value tuple;
    tuple.dict_id = dict_id;
    tuple.data = std::move(data);
    return tuple;
}

static tuple_cpr::value CprCodes(std::string &obj) {
    tuple_cpr::value tuple;
    Decode(obj, tuple);
    return tuple;
}

// -------------------------- Helper: Tuple to Raman Format -------------------------------------
static vector_of_string ToRamanFormat(const stock::value &stock) {
    std::vector <std::string> ret{std::to_string(stock.s_quantity), std::to_string(stock.s_ytd),
                                  std::to_string(stock.s_order_cnt), std::to_string(stock.s_remote_cnt)};
    return std::move(ret);
}

static vector_of_string ToRamanFormat(const stock_data::value &stock_data) {
    std::vector <std::string> ret{stock_data.s_dist_01.str(), stock_data.s_dist_02.str(), stock_data.s_dist_03.str(),
                                  stock_data.s_dist_04.str(), stock_data.s_dist_05.str(), stock_data.s_dist_06.str(),
                                  stock_data.s_dist_07.str(), stock_data.s_dist_08.str(), stock_data.s_dist_09.str(),
                                  stock_data.s_dist_10.str(), stock_data.s_data.str()};
    return std::move(ret);
}

static vector_of_string ToRamanFormat(const order_line::value &orderline) {
    std::vector <std::string> ret{std::to_string(orderline.ol_quantity), std::to_string(orderline.ol_amount),
                                  std::to_string(orderline.ol_delivery_d), std::to_string(orderline.ol_i_id),
                                  std::to_string(orderline.ol_supply_w_id), orderline.ol_dist_info.str()};
    return std::move(ret);
}

static vector_of_string ToRamanFormat(const customer::value &customer) {
    std::vector <std::string> ret{std::to_string(customer.c_discount),
                                  customer.c_credit.str(),
                                  customer.c_last.str(),
                                  customer.c_first.str(),
                                  std::to_string(customer.c_credit_lim),
                                  std::to_string(customer.c_balance),
                                  std::to_string(customer.c_ytd_payment),
                                  std::to_string(customer.c_payment_cnt),
                                  std::to_string(customer.c_delivery_cnt),
                                  customer.c_street_1.str(),
                                  customer.c_street_2.str(),
                                  customer.c_city.str(),
                                  customer.c_state.str(),
                                  customer.c_zip.str(),
                                  customer.c_phone.str(),
                                  std::to_string(customer.c_since),
                                  customer.c_middle.str(),
                                  customer.c_data.str()};
    return std::move(ret);
}

static vector_of_string ToRamanFormat(const oorder::value &order) {
    std::vector <std::string> ret{std::to_string(order.o_c_id),
                                  std::to_string(order.o_carrier_id),
                                  std::to_string(order.o_ol_cnt),
                                  std::to_string(order.o_all_local),
                                  std::to_string(order.o_entry_d)};
    return std::move(ret);
}

static vector_of_string ToRamanFormat(const history::value &history) {
    std::vector <std::string> ret{std::to_string(history.h_amount), history.h_data.str()};
    return std::move(ret);
}

static void FromRamanFormat(vector_of_string &raman_sample, stock::value &stock) {
    stock.s_quantity = std::stoi(raman_sample[0]);
    stock.s_ytd = std::stoi(raman_sample[1]);
    stock.s_order_cnt = std::stoi(raman_sample[2]);
    stock.s_remote_cnt = std::stoi(raman_sample[3]);
}

static void FromRamanFormat(vector_of_string &sample, stock_data::value &stock) {
    stock.s_dist_01 = std::move(sample[0]);
    stock.s_dist_02 = std::move(sample[1]);
    stock.s_dist_03 = std::move(sample[2]);
    stock.s_dist_04 = std::move(sample[3]);
    stock.s_dist_05 = std::move(sample[4]);
    stock.s_dist_06 = std::move(sample[5]);
    stock.s_dist_07 = std::move(sample[6]);
    stock.s_dist_08 = std::move(sample[7]);
    stock.s_dist_09 = std::move(sample[8]);
    stock.s_dist_10 = std::move(sample[9]);
    stock.s_data = std::move(sample[10]);
}

static void FromRamanFormat(vector_of_string &sample, order_line::value &orderline) {
    orderline.ol_quantity = std::stoi(sample[0]);
    orderline.ol_amount = std::stoi(sample[1]);
    orderline.ol_delivery_d = std::stoi(sample[2]);
    orderline.ol_i_id = std::stoi(sample[3]);
    orderline.ol_supply_w_id = std::stoi(sample[4]);
    orderline.ol_dist_info = std::move(sample[5]);
}

static void FromRamanFormat(vector_of_string &sample, customer::value &customer) {
    customer.c_discount = std::stoi(sample[0]);
    customer.c_credit = std::move(sample[1]);
    customer.c_last = std::move(sample[2]);
    customer.c_first = std::move(sample[3]);
    customer.c_credit_lim = std::stoi(sample[4]);
    customer.c_balance = std::stoi(sample[5]);
    customer.c_ytd_payment = std::stoi(sample[6]);
    customer.c_payment_cnt = std::stoi(sample[7]);
    customer.c_delivery_cnt = std::stoi(sample[8]);
    customer.c_street_1 = std::move(sample[9]);
    customer.c_street_2 = std::move(sample[10]);
    customer.c_city = std::move(sample[11]);
    customer.c_state = std::move(sample[12]);
    customer.c_zip = std::move(sample[13]);
    customer.c_phone = std::move(sample[14]);
    customer.c_since = std::stoi(sample[15]);
    customer.c_middle = std::move(sample[16]);
    customer.c_data = std::move(sample[17]);
}

static void FromRamanFormat(vector_of_string &sample, oorder::value &order) {
    order.o_c_id = std::stoi(sample[0]);
    order.o_carrier_id = std::stoi(sample[1]);
    order.o_ol_cnt = std::stoi(sample[2]);
    order.o_all_local = std::stoi(sample[3]);
    order.o_entry_d = std::stoi(sample[4]);
}

static void FromRamanFormat(vector_of_string &sample, history::value &history) {
    history.h_amount = std::stoi(sample[0]);
    history.h_data = std::move(sample[1]);
}

// -------------------------------- Raman -------------------------------------
template<typename T>
class RamanTable {
public:
    RamanTable() : sample_size_(sizeof(T)) {};

    inline ALWAYS_INLINE void PushTuple(const T &tuple) {
        table_.push_back(std::move(ToRamanFormat(tuple)));
    }

    inline ALWAYS_INLINE vector_of_string &GetTuple(size_t index) {
        return table_[index];
    }

    inline ALWAYS_INLINE void Clear() {
        table_.clear();
    }

    std::vector <vector_of_string> table_;
    size_t sample_size_;
};

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
    inline ALWAYS_INLINE T RamanDecompress(const std::string &bit_string) {
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

        T sample;
        FromRamanFormat(raman_sample, sample);
        return std::move(sample);
    }

    RamanCompressor *Copy() {
        return this;
    }

    uint32_t Size() {
        uint32_t ret = 0;
        for (auto &stat: stats_) ret += stat.BimapSize();
        for (auto &tree: forest_) ret += tree.Size();
        return ret;
    }

private:
    void SetNumFields(size_t num_fields) {
        stats_.resize(num_fields);
    }
};

// -------------------------------- For Block Compression -------------------------------------
template<typename T>
class RamanTupleBlock {
public:
    const size_t kBufferSize = 1024 * 16;

    RamanTupleBlock() : n_tuple(0), values_(kBufferSize), keys_(kBufferSize) {}

public:
    using key = typename T::key;
    using value = typename T::value;

    inline ALWAYS_INLINE bool Insert(const key &key, value &value) {
        keys_[n_tuple] = key;
        values_[n_tuple] = value;
        return ++n_tuple == kBufferSize;
    }

    uint64_t BlockCompress(std::vector <key> *keys, vector_of_string &compressed_values, uint64_t &dict_id) {
        // block learning
        std::vector <std::vector<std::string>> samples;
        for (auto &sample: values_) samples.push_back(ToRamanFormat(sample));
        RamanCompressor *cpr = new RamanCompressor();
        cpr->RamanLearning(samples);
        compressors_.push_back(cpr);

        // block compress
        for (auto &sample: values_) compressed_values.push_back(cpr->RamanCompress(sample));

        // get keys and dict id, and clear block
        keys = &keys_;
        dict_id = compressors_.size() - 1;
        n_tuple = 0;

        return cpr->Size();
    }

    inline ALWAYS_INLINE value &GetValue(key &key) {
        for (int32_t i = 0; i < n_tuple; ++i) {
            if (keys_[i] == key) return &values_[i];
        }
        return nullptr;
    }

    inline ALWAYS_INLINE RamanCompressor *GetCompressor(uint64_t dict_id) {
        if (dict_id >= compressors_.size())
            throw std::runtime_error("Invalid dict id in GetCompressor");
        return compressors_[dict_id];
    }

    inline ALWAYS_INLINE bool IsFull() {
        return n_tuple == kBufferSize;
    }

    inline ALWAYS_INLINE void AddCompressor(RamanCompressor *compressor) {
        compressors_.push_back(compressor);
    }

    inline ALWAYS_INLINE uint32_t Size() {
        uint32_t raman_dict_size = 0;
        for (auto *compressor: compressors_) raman_dict_size += compressor->Size();
        return raman_dict_size;
    }

private:
    int32_t n_tuple;
    std::vector<typename T::value> values_;
    std::vector<typename T::key> keys_;
    std::vector<RamanCompressor *> compressors_;
};