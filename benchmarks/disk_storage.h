#pragma once

#include <fcntl.h>
#include <string>
#include <sys/stat.h>
#include <unistd.h>
#include <utility>
#include <stdexcept>
#include <vector>
#include <random>

#include "../record/encoder.h"
#include "tpcc.h"

template<class T>
struct Tuple {
    T data_;            // in memory
    int32_t in_memory_;
    int64_t id_pos_;    // on disk
    int32_t id_thread_;

    Tuple() : in_memory_(false), data_(), id_pos_(-1), id_thread_(-1) {}

    inline ALWAYS_INLINE void Set(const T &data, bool in_memory = true, int64_t id_pos = 0, int64_t id_thread = 0) {
        data_ = data;
        in_memory_ = in_memory;
        id_pos_ = id_pos;
        id_thread_ = id_thread;
    }

    static inline ALWAYS_INLINE std::string &Serialize(std::string &s, const Tuple<T> &data) {
        ALWAYS_ASSERT(data.id_thread_ >= -1 && data.id_thread_ <= 256);
        ALWAYS_ASSERT(std::is_pod<Tuple<T>>::value);

        s.resize(sizeof(data));
        std::memcpy(&s[0], &data, sizeof(data));
        return s;
    }

    static inline ALWAYS_INLINE void Deserialize(const std::string &s, Tuple<T> &tuple) {
        ALWAYS_ASSERT(s.size() == sizeof(tuple));

        memcpy(&tuple, s.data(), sizeof(tuple));
    }
};

static inline ALWAYS_INLINE std::string &Serialize(std::string &s, const Tuple<std::string> &data) {
    ALWAYS_ASSERT((data.in_memory_ == 0 && data.id_thread_ >= 0 && data.id_pos_ >= 0) || data.in_memory_ == 1);
    // Clear the output string first
    s.clear();
    // Directly append the string data to the output string
    s.append(data.data_);
    // Serialize the last three members separately
    s.append(reinterpret_cast<const char *>(&data.in_memory_), sizeof(data.in_memory_));
    s.append(reinterpret_cast<const char *>(&data.id_pos_), sizeof(data.id_pos_));
    s.append(reinterpret_cast<const char *>(&data.id_thread_), sizeof(data.id_thread_));

    return s;
}

static inline ALWAYS_INLINE void Deserialize(const std::string &s, Tuple<std::string> &data) {
    size_t sz = sizeof(data.id_pos_) + sizeof(data.id_thread_) + sizeof(data.in_memory_);
    // Calculate the string size by subtracting 16 bytes from the total size
    size_t dataSize = s.size() - sz;
    // Extract string data
    data.data_.assign(s.data(), dataSize);
    // Deserialize the last three members separately
    const char *ptr = s.data() + dataSize;
    std::memcpy(&data.in_memory_, ptr, sizeof(data.in_memory_));
    ptr += sizeof(data.in_memory_);
    std::memcpy(&data.id_pos_, ptr, sizeof(data.id_pos_));
    ptr += sizeof(data.id_pos_);
    std::memcpy(&data.id_thread_, ptr, sizeof(data.id_thread_));

    ALWAYS_ASSERT((data.in_memory_ == 0 && data.id_thread_ >= 0 && data.id_pos_ >= 0) || data.in_memory_ == 1);
}

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
#endif

// ----------------------------- File Manager -----------------------------
struct FileDescriptor {
    int fd;
    std::mutex mutex;

    void *direct_io_buffer;
    SeqWriteBuffer write_buffer;

    FileDescriptor(const std::string &filename) : fd(DirectIOFile(filename)),
                                                  direct_io_buffer(aligned_alloc(BLOCKSIZE, DIRECT_IO_BUFFER_SIZE)) {}

    ~FileDescriptor() { if (fd != -1) close(fd); }

    template<typename T>
    void SeqDiskTupleWrite(T *data) {
        std::lock_guard <std::mutex> lock(mutex);
#if __APPLE__
        int64_t ret = write(fd, data, sizeof(T));
    if (ret < 0) throw std::runtime_error("write error in SeqDiskTupleWrite");
#elif __linux__
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
    int64_t DiskTupleRead(T *data, int64_t pos) {
        std::lock_guard <std::mutex> lock(mutex);
#if __APPLE__
        int64_t ret = pread(fd, data, sizeof(T), pos * sizeof(T));
    if (ret < 0) throw std::runtime_error("read error in DiskTupleRead");
    else return ret;
#elif __linux__
        // num of page = sizeof(T) / BlockSize + 1, but in our case, sizeof(T) cannot be larger than 4096
        int num_page = 1;
        if (pos * num_page < write_buffer.write_pos_) {
            // tuple is not in write buffer
            int64_t ret = pread(fd, direct_io_buffer, num_page * BLOCKSIZE, pos * num_page * BLOCKSIZE);
            if (ret < 0) {
                std::string error_msg = "read error in SeqDiskTupleWrite: " + std::string(strerror(errno));
                throw std::runtime_error(error_msg);
            }
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
    int64_t DiskTableSize() {
        std::lock_guard <std::mutex> lock(mutex);
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
        int32_t tuple_num = st_buf.st_size / (num_page * BLOCKSIZE);
#endif

//            // get size of each tuple
//            int64_t disk_size = 0;
//            T tuple;
//            for (int i = 0; i < tuple_num; ++i) {
//                int s = DiskTupleRead<T>(&tuple, i);
//                if (s != sizeof(T)) throw std::runtime_error("read error in DiskTableSize");
//                disk_size += Size(tuple);
//            }
//
//            return disk_size;
            return tuple_num * sizeof(T);
        }
    }

    // DirectIOFile moved here, now it's a static member function
    static int DirectIOFile(const std::string &table_name) {
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
};

class FileManager {
public:
    // delete copy constructor and copy assignment operator
    FileManager(const FileManager &) = delete;

    FileManager &operator=(const FileManager &) = delete;

    inline ALWAYS_INLINE static FileManager &GetInstance() {
        static FileManager instance;  // Guaranteed to be destroyed. Initialized on first use.
        return instance;
    }

    void AddFile(int64_t thread_id, const std::string &filename) {
        int64_t idx = Encode(thread_id, filename);

        // random seed
        std::random_device rd;
        std::mt19937 random_rng(rd());

        std::string name = std::to_string(thread_id) + "_" + filename + "_" + std::to_string(random_rng()) + ".tbl";
        files_[idx] = std::make_shared<FileDescriptor>(name);
    }

    /*
     * name code: 0 for customer, 1 for stock, 2 for order_line
     */
    inline ALWAYS_INLINE FileDescriptor &GetDescriptor(int64_t thread_id, int64_t name_code) {
        int64_t idx = (thread_id << 2) + name_code;
        if (files_.count(idx) == 0) throw std::runtime_error("Wrong thread id in FileManager::GetDescriptor");
        return *files_[idx];
    }

    int64_t Encode(int64_t thread, const std::string &filename) {
        ALWAYS_ASSERT(thread >= 0);
        if (filename == "customer") return (thread << 2) + 0;
        else if (filename == "stock") return (thread << 2) + 1;
        else if (filename == "order_line") return (thread << 2) + 2;
        else throw std::runtime_error("wrong filename in FileManager::Encode");
    }

    int64_t GetSize(int64_t thread) {
        int64_t size = 0;

        FileDescriptor &c_fd = GetDescriptor(thread, 0);
        size += c_fd.DiskTableSize<customer::value>();

        FileDescriptor &s_fd = GetDescriptor(thread, 1);
        size += s_fd.DiskTableSize<stock::value>();

        FileDescriptor &o_fd = GetDescriptor(thread, 2);
        size += o_fd.DiskTableSize<order_line::value>();

        return size;
    }

private:
    FileManager() {}  // private constructor so that it can't be called
    std::map <int64_t, std::shared_ptr<FileDescriptor>> files_;
};