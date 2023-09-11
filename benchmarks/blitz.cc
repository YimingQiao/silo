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
  std::random_device random_device;
  std::mt19937 mt19937(0);
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
