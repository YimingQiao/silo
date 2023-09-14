#include "blitz.h"

#include <random>

db_compress::CompressionConfig BlitzTable::CompressionConfig() {
  db_compress::CompressionConfig config;
  for (AttrConfig &ac: config_) config.allowed_err_.push_back(ac.tolerance);
  config.skip_model_learning_ = true;
  return config;
}

db_compress::Schema BlitzTable::Schema() {
  std::vector<int> attr_type;
  attr_type.reserve(config_.size());
  for (AttrConfig &ac: config_) attr_type.push_back(ac.type);
  return db_compress::Schema(attr_type);
}

void BlitzTable::RegisterAttrInterpreter() {
  for (int i = 0; i < config_.size(); ++i) {
    AttrConfig &ac = config_[i];
    if (ac.type == kEnum) db_compress::RegisterAttrInterpreter(i, new SimpleCategoricalInterpreter(ac.capacity));
    else
      db_compress::RegisterAttrInterpreter(i, new db_compress::AttrInterpreter());
  }

  // Register attributed model and interpreter
  RegisterAttrModel(0, new db_compress::TableCategoricalCreator());
  RegisterAttrModel(1, new db_compress::TableNumericalIntCreator());
  RegisterAttrModel(2, new db_compress::TableNumericalRealCreator());
  RegisterAttrModel(3, new db_compress::StringModelCreator());
}

void Blitzcrank::BlitzLearning(BlitzTable &table, db_compress::RelationCompressor &compressor) {
  // random number
  std::mt19937 mt19937(42);
  std::uniform_int_distribution<uint32_t> dist(0, table.RowsNum() - 1);
  bool tuning = false;

  // Learning Iterations
  while (true) {
    int tuple_cnt = 0;
    int tuple_random_cnt = 0;
    int tuple_idx;

    while (tuple_cnt < table.RowsNum()) {
      if (tuple_random_cnt < kNumEstSample) {
        tuple_idx = static_cast<int>(dist(mt19937));
        tuple_random_cnt++;
      } else {
        tuple_idx = tuple_cnt;
        tuple_cnt++;
      }

      db_compress::AttrVector &tuple = table.GetTuple(tuple_idx);
      { compressor.LearnTuple(tuple); }
      if (tuple_cnt >= kNonFullPassStopPoint && !compressor.RequireFullPass()) { break; }
    }
    compressor.EndOfLearningAndWriteModel();

    if (!tuning && compressor.RequireFullPass()) { tuning = true; }

    if (!compressor.RequireMoreIterationsForLearning()) { break; }
  }
}

// --------------------------- Enum Handle ----------------------------------
int EnumStrToId(const std::string &str, int32_t attr, const std::string &table_name) {
  int32_t idx = 0;
  if (table_name == "order line") idx = attr;
  else if (table_name == "stock")
    idx = OrderLineBlitz::kNumAttrs + attr;
  else if (table_name == "customer")
    idx = OrderLineBlitz::kNumAttrs + StockBlitz::kNumAttrs + attr;
  else
    printf("Unknown table name.\n");

  if (enum_map.size() <= idx) enum_map.resize(idx + 1);
  auto &enum2idx = enum_map[idx].enum2idx;
  auto &enums = enum_map[idx].enums;

  auto it = enum2idx.find(str);
  if (it != enum2idx.end()) return it->second;
  else {
    enum2idx[str] = enums.size();
    enums.push_back(str);
    return enums.size() - 1;
  }
}

std::string &EnumIdToStr(int32_t id, int32_t attr, const std::string &table_name) {
  int32_t map_idx = 0;
  if (table_name == "order line") map_idx = attr;
  else if (table_name == "stock")
    map_idx = OrderLineBlitz::kNumAttrs + attr;
  else if (table_name == "customer")
    map_idx = OrderLineBlitz::kNumAttrs + StockBlitz::kNumAttrs + StockDataBlitz::kNumAttrs + attr;
  else
    printf("Unknown table name.\n");

  assert(enum_map.size() > map_idx);
  db_compress::BiMap &map = enum_map[map_idx];
  assert(map.enums.size() > id);
  return map.enums[id];
}
