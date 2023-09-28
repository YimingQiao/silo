#include "../include/model.h"

#include <map>
#include <memory>

namespace db_compress {

    namespace {
        std::map<int, std::unique_ptr<ModelCreator>> model_rep;
        /**
             * model_ptr is the replicate of model_rep, but without being unique_ptr
             * makes it possible to return it directly.
             */
        std::map<int, ModelCreator *> model_ptr;

        /**
             * In TPC-C, I want to compress multiple tables at the same time. For each table, a map of attribute
             * interpreter is needed. Therefore, a vector of map is used.
             */
        size_t table_idx = 0;
        std::vector <std::map<int, std::unique_ptr < AttrInterpreter>>> interpreter_rep_vec(1);

    }// anonymous namespace

    void RegisterAttrModel(int attr_type, ModelCreator *creator) {
        std::unique_ptr <ModelCreator> ptr(creator);
        model_rep[attr_type] = std::move(ptr);
        model_ptr[attr_type] = creator;
    }

    ModelCreator *GetAttrModel(int attr_type) { return model_ptr[attr_type]; }

    void NextTableAttrInterpreter() {
        interpreter_rep_vec.emplace_back();
        table_idx++;
    }

    void RegisterAttrInterpreter(int attr_index, AttrInterpreter *interpreter) {
        std::map<int, std::unique_ptr<AttrInterpreter>> &interpreter_rep = interpreter_rep_vec[table_idx];
        interpreter_rep[attr_index].reset(interpreter);
    }

    const AttrInterpreter *GetAttrInterpreter(int attr_index) {
        std::map<int, std::unique_ptr<AttrInterpreter>> &interpreter_rep = interpreter_rep_vec[table_idx];
        if (interpreter_rep[attr_index] ==
            nullptr) { interpreter_rep[attr_index] = std::make_unique<AttrInterpreter>(); }
        return interpreter_rep[attr_index].get();
    }

    std::vector <size_t> GetPredictorCap(const std::vector <size_t> &pred) {
        std::vector <size_t> cap(pred.size());
        for (size_t i = 0; i < pred.size(); ++i) cap[i] = GetAttrInterpreter(static_cast<int>(pred[i]))->EnumCap();

        return cap;
    }

    SquIDModel::SquIDModel(const std::vector <size_t> &predictors, size_t target_var)
            : predictor_list_(predictors),
              predictor_list_size_(predictors.size()),
              target_var_(target_var) {}
}// namespace db_compress
