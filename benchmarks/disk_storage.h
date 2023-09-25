#pragma once

#include <fcntl.h>
#include <string>
#include <sys/stat.h>
#include <unistd.h>
#include <utility>
#include <stdexcept>
#include <vector>
#include "../record/encoder.h"

template<class T>
struct Tuple {
    T data_;            // in memory
    bool in_memory_;
    int32_t id_pos_;    // on disk
    int32_t id_thread_;

    Tuple() : in_memory_(false), data_(), id_pos_(-1), id_thread_(-1) {}

    inline ALWAYS_INLINE void Set(const T &data, bool in_memory, int64_t id_pos, int64_t id_thread) {
        data_ = data;
        in_memory_ = in_memory;
        id_pos_ = id_pos;
        id_thread_ = id_thread;
    }

    inline ALWAYS_INLINE void Set(const T &data) {
        data_ = data;
        in_memory_ = true;
        id_pos_ = -1;
        id_thread_ = -1;
    }

    static std::string Serialize(const Tuple<T> &data) {
        return std::string(reinterpret_cast<const char *>(&data), sizeof(data));
    }

    static inline ALWAYS_INLINE Tuple<T> Deserialize(const std::string &s) {
        Tuple<T> tuple;
        memcpy(&tuple, s.data(), sizeof(tuple));
        return tuple;
    }
};


#if __linux__
#define BLOCKSIZE 4096
#define DIRECT_IO_BUFFER_SIZE 4096

/**
 * This is a write buffer for sequence io.
 *
 * One tuple occupies at least one page.
 */
struct SeqWriteBuffer {
    static const int32_t kWriteBufferSize = 128;

    void *buf_dat_ = aligned_alloc(BLOCKSIZE, BLOCKSIZE * kWriteBufferSize);
    int64_t write_pos_ = 0;
    int32_t num_filled_page = 0;

    SeqWriteBuffer() = default;
};

namespace {
    std::vector<SeqWriteBuffer> write_buffers;

    void *direct_io_buffer = aligned_alloc(BLOCKSIZE, BLOCKSIZE);
}
#endif

__attribute__((__used__)) static inline int DirectIOFile(const std::string &table_name) {
#if __APPLE__
    int fd = open(table_name.c_str(), O_RDWR | O_CREAT, 0666);
    fcntl(fd, F_NOCACHE, 1);
#elif __linux__
    int flag = O_RDWR | O_CREAT | O_DIRECT;
    int fd = open(table_name.c_str(), flag, 0666);
#endif
    if (fd < 0)
        throw std::runtime_error("open file error in DirectIOFile");
    return fd;
}

template<typename T>
static inline void DiskTupleWrite(int fd, T *data, int64_t pos) {
#if __APPLE__
    int64_t ret = pwrite(fd, data, sizeof(T), pos * sizeof(T));
    if (ret < 0) throw std::runtime_error("write error in SeqDiskTupleWrite");
#elif __linux__
    if (sizeof(T) > DIRECT_IO_BUFFER_SIZE)
        throw std::runtime_error("direct io buffer size is less than sizeof(T) in SeqDiskTupleWrite");

    memcpy(direct_io_buffer, data, sizeof(T));
    // num of page = sizeof(T) / BlockSize + 1, but in our case, sizeof(T) cannot be larger than 4096
    int num_page = 1;
    int64_t ret = pwrite(fd, direct_io_buffer, 512, pos * num_page * BLOCKSIZE);
    if (ret < 0) throw std::runtime_error("write error in SeqDiskTupleWrite");
#endif
}

template<typename T>
static inline void SeqDiskTupleWrite(int fd, T *data) {
#if __APPLE__
    int64_t ret = write(fd, data, sizeof(T));
    if (ret < 0) throw std::runtime_error("write error in SeqDiskTupleWrite");
#elif __linux__
    // get write buffer of fd.
    if (write_buffers.size() < fd - 2) write_buffers.resize(fd - 2);
    SeqWriteBuffer &write_buffer = write_buffers[fd - 3];

    // write buffer is full
    // num of page = sizeof(T) / BlockSize + 1, but in our case, sizeof(T) cannot be larger than 4096
    int num_page = 1;
    if (write_buffer.num_filled_page == SeqWriteBuffer::kWriteBufferSize) {
        int64_t ret = write(fd, write_buffer.buf_dat_, write_buffer.num_filled_page * BLOCKSIZE);
        if (ret < 0) throw std::runtime_error("write error in SeqDiskTupleWrite");
        write_buffer.num_filled_page = 0;
        write_buffer.write_pos_ += SeqWriteBuffer::kWriteBufferSize;
    }

    // write to buffer
    memcpy((char *) write_buffer.buf_dat_ + write_buffer.num_filled_page * BLOCKSIZE, data, sizeof(T));
    write_buffer.num_filled_page += num_page;
#endif
}

template<typename T>
static inline int64_t DiskTupleRead(int fd, T *data, int64_t pos) {
#if __APPLE__
    int64_t ret = pread(fd, data, sizeof(T), pos * sizeof(T));
    if (ret < 0) throw std::runtime_error("read error in DiskTupleRead");
    else return ret;
#elif __linux__
    // get write buffer of fd.
    if (write_buffers.size() < fd - 2) throw std::runtime_error("read error in DiskTupleRead");
    SeqWriteBuffer &write_buffer = write_buffers[fd - 3];

    // num of page = sizeof(T) / BlockSize + 1, but in our case, sizeof(T) cannot be larger than 4096
    int num_page = 1;
    if (pos * num_page < write_buffer.write_pos_) {
        // tuple is not in write buffer
        int64_t ret = pread(fd, direct_io_buffer, num_page * BLOCKSIZE, pos * num_page * BLOCKSIZE);
        if (ret < 0) throw std::runtime_error("read error in SeqDiskTupleWrite");
        else {
            memcpy(data, direct_io_buffer, sizeof(T));
            return sizeof(T);
        }
    } else {
        // tuple is in write buffer or out of range.
        if (pos * num_page >= write_buffer.write_pos_ + write_buffer.num_filled_page)
            throw std::runtime_error("Read out of range in DiskTupleRead");

        int32_t idx = pos * num_page - write_buffer.write_pos_;
        memcpy(data, (char *) write_buffer.buf_dat_ + idx * BLOCKSIZE, sizeof(T));
        return sizeof(T);
    }
#endif
}

template<typename T>
static inline int64_t DiskTableSize(int fd) {
    // get #tuple
    struct stat st_buf;
    if (fstat(fd, &st_buf) == -1) {
        switch (errno) {
            case EBADF:
                throw std::runtime_error("fd is not a valid file descriptor");
            case EFAULT:
                throw std::runtime_error("std buffer is outside of your accessible address space");
            default:
                throw std::runtime_error("fstat error in DiskTableSize");
        }
    } else {
#if __APPLE__
        int32_t tuple_size = st_buf.st_size / sizeof(T);
#elif __linux__
        // num of page = sizeof(T) / BlockSize + 1, but in our case, sizeof(T) cannot be larger than 4096
        int num_page = 1;
        int32_t tuple_size = st_buf.st_size / (num_page * BLOCKSIZE);
#endif

        // get size of each tuple
        int64_t disk_size = 0;
        T tuple;
        for (int i = 0; i < tuple_size; ++i) {
            int s = DiskTupleRead(fd, &tuple, i);
            if (s != sizeof(T)) throw std::runtime_error("read error in DiskTableSize");
            disk_size += tuple.size();
        }

        return disk_size;
    }
}

template<typename T>
static inline int64_t DiskTableSize(const std::string &file_name) {
    int fd = DirectIOFile(file_name);
    return DiskTableSize<T>(fd);
}
