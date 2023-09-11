#pragma once

#include "../third-party/libblitz/include/base.h"
#include "../third-party/libblitz/include/compression.h"
#include "../third-party/libblitz/include/decompression.h"
#include "../third-party/libblitz/include/model.h"
#include "../third-party/libblitz/include/model_learner.h"
#include "../util.h"
#include "tpcc.h"

#define kEnum 0
#define kInteger 1
#define kDouble 2
#define kString 3

namespace {
  static db_compress::AttrVector stock_buffer(4);
  stock::value stock_value;

  static db_compress::AttrVector stock_data_buffer(11);
  stock_data::value stock_data_value;
}// namespace

/**
 * This class is used to interpret categorical attributes.
 */
class SimpleCategoricalInterpreter : public db_compress::AttrInterpreter {
private:
  int cap_;

public:
  explicit SimpleCategoricalInterpreter(int cap) : cap_(cap) {}

  bool EnumInterpretable() const override { return true; }

  int EnumCap() const override { return cap_; }

  size_t EnumInterpret(const db_compress::AttrValue &attr) const override { return attr.Int(); }
};

struct AttrConfig {
  int type;
  int capacity;
  double tolerance;
};


// -------------------------- Blitz Table ------------------------------------

class BlitzTable {
public:
  explicit BlitzTable(size_t num_attrs) : buffer_(num_attrs) {}

public:
  db_compress::CompressionConfig CompressionConfig();

  db_compress::Schema Schema();

  inline ALWAYS_INLINE uint32_t RowsNum() { return table_.size(); }

  inline ALWAYS_INLINE db_compress::AttrVector &GetTuple(uint32_t idx) {
    assert(idx < table_.size());
    return table_[idx];
  }

  inline ALWAYS_INLINE void Clear() { table_.clear(); }

protected:
  db_compress::AttrVector buffer_;
  std::vector<db_compress::AttrVector> table_;
  std::vector<AttrConfig> config_;

  void RegisterAttrInterpreter();
};

class StockBlitz : public BlitzTable {
public:
  static const int kNumAttrs = 4;

public:
  StockBlitz() : BlitzTable(kNumAttrs) {
    config_ = {
        {kEnum, 100, 0},
        {kInteger, 0, 0.5},
        {kEnum, 2000, 0},
        {kEnum, 100, 0},
    };
    RegisterAttrInterpreter();
  }

  inline ALWAYS_INLINE bool PushTuple(stock::value &stock) {
    buffer_.attr_[0].value_ = (int) stock.s_quantity;
    buffer_.attr_[1].value_ = (int) stock.s_ytd;
    buffer_.attr_[2].value_ = (int) stock.s_order_cnt;
    buffer_.attr_[3].value_ = (int) stock.s_remote_cnt;

    table_.push_back(buffer_);
    return true;
  }
};

class StockDataBlitz : public BlitzTable {
public:
  static const int kNumAttrs = 11;

public:
  StockDataBlitz() : BlitzTable(kNumAttrs) {
    config_ = {
        {kString, 0, 0}, {kString, 0, 0}, {kString, 0, 0}, {kString, 0, 0}, {kString, 0, 0}, {kString, 0, 0},
        {kString, 0, 0}, {kString, 0, 0}, {kString, 0, 0}, {kString, 0, 0}, {kString, 0, 0},
    };
    RegisterAttrInterpreter();
  }

  bool PushTuple(stock_data::value &stock_data) {
    buffer_.attr_[0].value_ = stock_data.s_data.str();
    buffer_.attr_[1].value_ = stock_data.s_dist_01.str();
    buffer_.attr_[2].value_ = stock_data.s_dist_02.str();
    buffer_.attr_[3].value_ = stock_data.s_dist_03.str();
    buffer_.attr_[4].value_ = stock_data.s_dist_04.str();
    buffer_.attr_[5].value_ = stock_data.s_dist_05.str();
    buffer_.attr_[6].value_ = stock_data.s_dist_06.str();
    buffer_.attr_[7].value_ = stock_data.s_dist_07.str();
    buffer_.attr_[8].value_ = stock_data.s_dist_08.str();
    buffer_.attr_[9].value_ = stock_data.s_dist_09.str();
    buffer_.attr_[10].value_ = stock_data.s_dist_10.str();

    table_.push_back(buffer_);
    return true;
  }
};

class Blitzcrank {
public:
  db_compress::RelationCompressor *cpr_;
  db_compress::RelationDecompressor *dpr_;

  explicit Blitzcrank(const std::string &name)
      : name_(std::to_string(rand()) + "_" + name + "_model.blitz"),
        cpr_(nullptr),
        dpr_(nullptr) {}

  Blitzcrank(const Blitzcrank &other) {
    name_ = other.name_;
    cpr_ = other.cpr_;
    dpr_ = other.dpr_;
  }

  void Train(BlitzTable &table) {
    cpr_ = new db_compress::RelationCompressor(name_.c_str(), table.Schema(), table.CompressionConfig(), kBlockSize);
    BlitzLearning(table, *cpr_);
    dpr_ = new db_compress::RelationDecompressor(name_.c_str(), table.Schema(), kBlockSize);
    dpr_->InitWithoutIndex();

    std::cerr << "[INFO - Blitzcrank] Compressor for " << name_ << " trained." << std::endl;
  }

private:
  std::string name_;

  static void BlitzLearning(BlitzTable &table, db_compress::RelationCompressor &compressor);
};

static inline ALWAYS_INLINE db_compress::AttrVector &ToAttrVector(stock::value &stock) {
  stock_buffer.attr_[0].value_ = (int) stock.s_quantity;
  stock_buffer.attr_[1].value_ = (int) stock.s_ytd;
  stock_buffer.attr_[2].value_ = (int) stock.s_order_cnt;
  stock_buffer.attr_[3].value_ = (int) stock.s_remote_cnt;
  return stock_buffer;
}

static inline ALWAYS_INLINE stock::value *ToStock(db_compress::AttrVector &attr_vector) {
  stock::value &stock = stock_value;
  stock.s_quantity = attr_vector.attr_[0].Int();
  stock.s_ytd = attr_vector.attr_[1].Int();
  stock.s_order_cnt = attr_vector.attr_[2].Int();
  stock.s_remote_cnt = attr_vector.attr_[3].Int();
  return &stock;
}

static inline ALWAYS_INLINE db_compress::AttrVector &ToAttrVector(stock_data::value &stock_data) {
  stock_data_buffer.attr_[0].value_ = stock_data.s_data.str();
  stock_data_buffer.attr_[1].value_ = stock_data.s_dist_01.str();
  stock_data_buffer.attr_[2].value_ = stock_data.s_dist_02.str();
  stock_data_buffer.attr_[3].value_ = stock_data.s_dist_03.str();
  stock_data_buffer.attr_[4].value_ = stock_data.s_dist_04.str();
  stock_data_buffer.attr_[5].value_ = stock_data.s_dist_05.str();
  stock_data_buffer.attr_[6].value_ = stock_data.s_dist_06.str();
  stock_data_buffer.attr_[7].value_ = stock_data.s_dist_07.str();
  stock_data_buffer.attr_[8].value_ = stock_data.s_dist_08.str();
  stock_data_buffer.attr_[9].value_ = stock_data.s_dist_09.str();
  stock_data_buffer.attr_[10].value_ = stock_data.s_dist_10.str();
  return stock_data_buffer;
}

static inline ALWAYS_INLINE stock_data::value* ToStockData(db_compress::AttrVector &attr_vector) {
  stock_data::value& stock_data = stock_data_value;
  stock_data.s_data = attr_vector.attr_[0].String();
  stock_data.s_dist_01 = attr_vector.attr_[1].String();
  stock_data.s_dist_02 = attr_vector.attr_[2].String();
  stock_data.s_dist_03 = attr_vector.attr_[3].String();
  stock_data.s_dist_04 = attr_vector.attr_[4].String();
  stock_data.s_dist_05 = attr_vector.attr_[5].String();
  stock_data.s_dist_06 = attr_vector.attr_[6].String();
  stock_data.s_dist_07 = attr_vector.attr_[7].String();
  stock_data.s_dist_08 = attr_vector.attr_[8].String();
  stock_data.s_dist_09 = attr_vector.attr_[9].String();
  stock_data.s_dist_10 = attr_vector.attr_[10].String();
  return &stock_data;
}

static inline ALWAYS_INLINE db_compress::AttrVector &StockBuffer() { return stock_buffer; }
