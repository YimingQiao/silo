#pragma once

#include <vector>
#include <string>
#include <iostream>

#include "../third-party/libzstd/zstd.h"
#include "../third-party/libzstd/zdict.h"
#include "../third-party/libzstd/common.h"
#include "../macros.h"

template<typename T>
class ZSTDTable {
public:
    ZSTDTable() : sample_size_(sizeof(T)) {};

    inline ALWAYS_INLINE void PushTuple(const T &tuple) { table_.push_back(tuple); }

    inline ALWAYS_INLINE T &GetTuple(size_t index) { return table_[index]; }

    inline ALWAYS_INLINE void Clear() { table_.clear(); }

    std::vector <T> table_;
    size_t sample_size_;
};

template<typename T>
class ZSTD {
public:
    static const int kDictCapacity = 5 * 110 * 1024;
    static const int kCompressLevel = 3;

public:
    ZSTD() : cctx_(ZSTD_createCCtx()), dctx_(ZSTD_createDCtx()), dict_buffer_(malloc_orDie(kDictCapacity)),
             dict_size_(0), codes(ZSTD_compressBound(sizeof(T)), '\0') {}

    void Train(ZSTDTable<T> &table) {
        std::vector <T> &samples = table.table_;
        std::vector <size_t> sample_sizes(samples.size(), table.sample_size_);

        dict_size_ = ZDICT_trainFromBuffer(dict_buffer_, kDictCapacity,
                                           samples.data(), sample_sizes.data(),
                                           samples.size());
        if (ZDICT_isError(dict_size_)) {
            std::cout << "Error: " << ZDICT_getErrorName(dict_size_) << std::endl;
            exit(1);
        }
        cdict_ = ZSTD_createCDict(dict_buffer_, dict_size_, kCompressLevel);
        ddict_ = ZSTD_createDDict(dict_buffer_, dict_size_);
    }

    inline ALWAYS_INLINE std::string ZstdCompress(const T &src) {
        std::string codes(ZSTD_compressBound(sizeof(T)), '\0');
        size_t code_size = ZSTD_compress_usingCDict(cctx_, codes.data(), codes.size(), &src, sizeof(T), cdict_);
        ALWAYS_ASSERT(!ZSTD_isError(code_size));
        if (ZSTD_isError(code_size)) CHECK_ZSTD(code_size);

        return codes.substr(0, code_size);
    }

    inline ALWAYS_INLINE void ZstdDecompress(const std::string &src, T *data) {
        size_t ret = ZSTD_decompress_usingDDict(dctx_, data, sizeof(T), src.data(), src.size(), ddict_);
        ALWAYS_ASSERT(!ZSTD_isError(ret));
        // if (ZSTD_isError(ret)) CHECK_ZSTD(ret);
    }

    inline ALWAYS_INLINE ZSTD *Copy() {
        ZSTD *ret = new ZSTD<T>();
        ret->cdict_ = ZSTD_createCDict(dict_buffer_, dict_size_, kCompressLevel);
        ret->ddict_ = ZSTD_createDDict(dict_buffer_, dict_size_);
        return ret;
    }

private:
    ZSTD_CCtx *const cctx_;
    ZSTD_DCtx *const dctx_;

    ZSTD_CDict_s *cdict_;
    ZSTD_DDict_s *ddict_;

    void *dict_buffer_;
    size_t dict_size_;

    std::string codes;
};
