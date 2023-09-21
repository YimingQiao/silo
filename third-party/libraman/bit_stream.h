#pragma once

#include <istream>
#include <ostream>
#include <vector>

class BitStream {
public:
    BitStream() : bits_(streamSize * 8), n_bits_(0) {}

    inline std::string ToString() const {
        const size_t numBytes = (bits_.size() + 7) / 8;
        std::string result(numBytes, 0);

        int pos = 0;  // Position in bits_
        for (size_t i = 0; i < numBytes; ++i) {
            unsigned char byte = 0;
            for (int j = 0; j < 8 && pos < bits_.size(); ++j, ++pos) {
                byte = (byte << 1) | bits_[pos];
            }
            result[i] = byte;
        }

        return result;
    }

    inline uint32_t size() const { return n_bits_ >> 3; }

    inline void Clear() { n_bits_ = 0; }

    inline bool GetBit(size_t idx) const {
        if (idx >= n_bits_) throw std::logic_error("Index out of bounds");
        return bits_[idx];
    }

    inline void SetBit(size_t idx, bool val) {
        if (idx >= n_bits_) throw std::logic_error("Index out of bounds");
        bits_[idx] = val;
    }

    inline void WriteBit(bool val) {
        if (n_bits_ == streamSize * 8) {
            streamSize *= 2;
            bits_.resize(streamSize * 8);
        }
        bits_[n_bits_++] = val;
    }

    inline void WriteBits(const std::vector<bool> &bits) {
        for (bool bit: bits) WriteBit(bit);
    }

    inline void InitBits(uint32_t delta, size_t n_bits) {
        n_bits_ = 0;

        for (size_t i = 0; i < n_bits; ++i) {
            WriteBit(delta & (1 << (n_bits - i - 1)));
        }
    }

    uint32_t GetLogR(size_t logR) const {
        uint32_t ret = 0;
        for (size_t i = 0; i < logR; ++i) {
            ret = (ret << 1) | GetBit(i);
        }
        return ret;
    }

    BitStream SubStream(size_t start, size_t len) const {
        BitStream stream;
        stream.bits_.resize((len + 7) >> 3);
        for (size_t i = 0; i < len; ++i) stream.WriteBit(GetBit(start + i));
        return stream;
    }

    bool operator<(const BitStream &other) const {
        size_t i = 0;
        while (i < n_bits_ && i < other.n_bits_) {
            if (GetBit(i) != other.GetBit(i)) return GetBit(i) < other.GetBit(i);
            i++;
        }
        return n_bits_ < other.n_bits_;
    }

    BitStream operator-(const BitStream &other) const {
        BitStream stream;
        stream.bits_.resize((n_bits_ + 7) >> 3);
        stream.n_bits_ = n_bits_;
        bool carry = false;
        for (int i = n_bits_ - 1; i >= 0; i--) {
            // minus
            stream.SetBit(i, GetBit(i) ^ other.GetBit(i) ^ carry);
            carry = (GetBit(i) && carry) || (GetBit(i) && other.GetBit(i)) ||
                    (carry && other.GetBit(i));
        }
        return stream;
    }

    BitStream operator+(const BitStream &other) const {
        BitStream stream;
        stream.bits_.resize((n_bits_ + 7) >> 3);
        stream.n_bits_ = n_bits_;
        bool carry = false;
        for (int i = n_bits_ - 1; i >= 0; i--) {
            // plus
            stream.SetBit(i, GetBit(i) ^ other.GetBit(i) ^ carry);
            carry = (GetBit(i) && other.GetBit(i)) || (carry && other.GetBit(i)) ||
                    (carry && GetBit(i));
        }
        return stream;
    }

    BitStream &operator|=(const BitStream &other) {
        if (n_bits_ != other.n_bits_)
            throw std::logic_error("BitStreams must be the same length");
        for (size_t i = 0; i < n_bits_; ++i) SetBit(i, GetBit(i) | other.GetBit(i));
        return *this;
    }

    BitStream &operator+=(const BitStream &other) {
        for (size_t i = 0; i < other.n_bits_; ++i) WriteBit(other.GetBit(i));
        return *this;
    }

    bool operator!=(const BitStream &other) const {
        if (n_bits_ != other.n_bits_) return true;
        for (size_t i = 0; i < n_bits_; ++i)
            if (GetBit(i) != other.GetBit(i)) return true;
        return false;
    }

private:
    size_t streamSize = 8;
    std::vector<bool> bits_;
    size_t n_bits_ = 0;
};
