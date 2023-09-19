#pragma once

#include <vector>
#include <string>
#include <iostream>

#include "../third-party/libzstd/zstd.h"
#include "../third-party/libzstd/zdict.h"
#include "../third-party/libzstd/common.h"

template<typename T>
class ZSTDTable {
public:
    ZSTDTable() : sample_size_(sizeof(T)) {};

    void PushTuple(const T &tuple) {
        table_.push_back(tuple);
    }

    T &GetTuple(size_t index) {
        return table_[index];
    }

    void Clear() {
        table_.clear();
    }

    std::vector <T> table_;
    size_t sample_size_;
};

template<typename T>
class ZSTD {
public:
    static const int kDictCapacity = 5 * 110 * 1024;
    static const int kCompressLevel = 3;

public:
    ZSTD() : cctx_(ZSTD_createCCtx()), dctx_(ZSTD_createDCtx()) {}

    void Train(ZSTDTable<T> &table) {
        std::vector <T> &samples = table.table_;
        std::vector <size_t> sample_sizes(samples.size(), table.sample_size_);

        void *dict_buffer = malloc_orDie(kDictCapacity);
        size_t dict_size = ZDICT_trainFromBuffer(dict_buffer, kDictCapacity,
                                                 samples.data(), sample_sizes.data(),
                                                 samples.size());
        if (ZDICT_isError(dict_size)) {
            std::cout << "Error: " << ZDICT_getErrorName(dict_size) << std::endl;
            exit(1);
        }
        cdict_ = ZSTD_createCDict(dict_buffer, dict_size, kCompressLevel);
        ddict_ = ZSTD_createDDict(dict_buffer, dict_size);
    }

    std::string ZstdCompress(T &src) {
        size_t code_capacity = ZSTD_compressBound(sizeof(T));
        std::string code_buffer(code_capacity, '\0');
        size_t code_size = ZSTD_compress_usingCDict(cctx_, code_buffer.data(), code_capacity,
                                                    &src, sizeof(T), cdict_);
        return std::move(code_buffer.substr(0, code_size));
    }

    void ZstdDecompress(T *data, std::string &src) {
        int ret = ZSTD_decompress_usingDDict(dctx_, data, sizeof(T), src.data(), src.size(), ddict_);
        if (ret < 0)
            CHECK_ZSTD(ret);
    }

    ZSTD *Copy() {
        ZSTD *ret = new ZSTD();
        ret->cdict_ = cdict_;
        ret->ddict_ = ddict_;
        return ret;
    }

private:
    ZSTD_CCtx *const cctx_;
    ZSTD_DCtx *const dctx_;

    ZSTD_CDict_s *cdict_;
    ZSTD_DDict_s *ddict_;
};
