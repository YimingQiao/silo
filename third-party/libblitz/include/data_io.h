/**
 * @file data_io.h
 * @brief Header file for data IO.
 */

#ifndef DATA_IO_H
#define DATA_IO_H

#include <fstream>
#include <iostream>
#include <memory>
#include <vector>

#include "base.h"

namespace db_compress {

/**
 * SequenceByteWriter is a utility class that can be used to write bit strings
 * in sequence.
 */
class SequenceByteWriter {
 public:
  /**
   * Create a SequenceByteWriter.
   *
   * @param file_name compressed file address, user specified
   */
  explicit SequenceByteWriter(const std::string &file_name);

  /**
   * Deconstruct a SequenceByteWriter.
   */
  ~SequenceByteWriter();

  /**
   * Write the least significant (len) bits
   *
   * @param byte a byte to be written partly
   * @param len length of bits to be written from left to right
   */
  void WriteLess(unsigned char byte, size_t len);

  /**
   * Write a byte at once.
   *
   * @param byte a byte to be written
   */
  void WriteByte(unsigned char byte);

  /**
   * Write 16 bits at once.
   *
   * @param val unsigned int is 32 bits, write the lower 16 bits
   */
  void Write16Bit(unsigned int val);

  /**
   * Write 32 bits at once.
   *
   * @param byte byte is an array of 4 char
   */
  void Write32Bit(unsigned char byte[4]);

  /**
   * Write 32 bits at once.
   *
   * @param data it is 64 bits, write the lower 32 bits
   */
  void Write32Bit(unsigned int data);

  /**
   * Write a uint_64
   */
  void WriteUint64(uint64_t data);

  uint64_t GetNumBits() { return num_bits_; }

  void ClearNumBits() { num_bits_ = 0; }

 private:
  std::ofstream file_;
  // 64 KB buffer
  char buffer_[65537];
  // 0 - 8191 * 8 (8192 * 8)
  uint64_t bits_counter_;

  // stats
  uint64_t num_bits_{0};
};

/**
 * ByteReader firstly loads all data into memory, then output data from memory.
 */
class ByteReader {
 public:
  /**
   * Create a in-memory byte reader
   *
   * @param file_name compressed file address
   */
  explicit ByteReader(const std::string &file_name) {
    std::ifstream fin(file_name, std::ios::binary);
    if (!fin.is_open()) std::cout << "Cannot open file " << file_name << "\n";
    while (!fin.eof()) init_data_.push_back(fin.get());
    // pop the last byte '255'.
    init_data_.pop_back();
    stream_ = &init_data_;
    fin.close();
  }

  /**
   * Read a byte.
   *
   * @return return a unsigned char of 8 bits
   */
  inline uint8_t ReadByte() {
    assert(byte_pos_ < stream_->size());
    return (*stream_)[byte_pos_++];
  }

  /**
   * Read 16 bits.
   *
   * @return return a unsigned int of 16 bits, the result is in the lower 16
   * bits.
   */
  inline uint16_t Read16Bit() {
    uint16_t ret = ReadByte();
    ret = (ret << 8) | ReadByte();

    return ret;
  }

  uint32_t Read32Bit() { return (Read16Bit() << 16) + Read16Bit(); }

  /**
   * Read 32 bits.
   *
   * @param bytes return an unsigned char array of length 4
   */
  void Read32Bit(unsigned char *bytes) {
    for (int i = 0; i < 4; ++i) bytes[i] = ReadByte();
  }

  /**
   * Read an uint_64 number
   */
  uint64_t ReadUint64() {
    uint64_t high = Read32Bit();
    uint32_t low = Read32Bit();

    return (high << 32) + low;
  }

  /**
   * Sets the position of the next character to be extracted from the input
   * stream. The next position is 8 * num_bytes_ + num_bits_ bits relative to
   * current position.
   *
   * @param num_bytes distance between current position and next character to
   * read in bytes.
   * @param num_bits how many bits left to reach the desired position
   * @param way this parameter is the same as input way in function 'seekg'
   */
  inline void Seekg(int64_t num_bytes, std::ios_base::seekdir way) {
    if (way == std::ios_base::beg)
      byte_pos_ = num_bytes;
    else if (way == std::ios_base::end)
      byte_pos_ = stream_->size() + num_bytes;
    else if (way == std::ios_base::cur)
      byte_pos_ += num_bytes;
  }

  inline void SetPos(uint64_t pos) { byte_pos_ = pos; }

  inline uint64_t Tellg() { return byte_pos_; }

  inline void FillStream(std::vector<uint8_t> *bytes) {
    stream_ = bytes;
    byte_pos_ = 0;
  }

 private:
  std::vector<uint8_t> *stream_;
  std::vector<uint8_t> init_data_;
  uint32_t byte_pos_{0};
};

}  // namespace db_compress

#endif
