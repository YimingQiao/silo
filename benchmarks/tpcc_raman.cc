#include "tpcc_raman.h"

void RamanCompressor::RamanLearning(std::vector <std::vector<std::string>> &samples) {
    {
        util::scoped_timer time("RamanLearning", true, &training_time_);
        if (samples.empty()) throw std::runtime_error("Empty sample set in RamanLearning");
        size_t num_fields = samples[0].size();

        // stats
        SetNumFields(num_fields);
        for (auto &sample: samples) {
            for (size_t i = 0; i < num_fields; ++i) stats_[i].Increment(sample[i]);
        }

        // code tree
        for (size_t i = 0; i < num_fields; ++i) {
            raman::CodeTree tree = stats_[i].BuildCodeTree();
            raman::CanonicalCode code(tree, stats_[i].getSymbolLimit());
            forest_.push_back(code.toCodeTree());
        }
    }
}
