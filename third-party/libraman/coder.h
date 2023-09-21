#ifndef RAMAN_CODER_H
#define RAMAN_CODER_H

#include <stdexcept>

#include "bit_stream.h"
#include "code_tree.h"

namespace raman {

    template<typename BitGetter>
    static inline void Decode(size_t &sym, CodeTree *code_tree, BitGetter getBit) {
        if (code_tree == nullptr) throw std::logic_error("Code tree is null");

        const InternalNode *current = &code_tree->root_;
        while (true) {
            bool bit = getBit();
            const Node *next;

            if (bit)
                next = current->r_.get();
            else
                next = current->l_.get();

            if (dynamic_cast<const Leaf *>(next) != nullptr) {
                sym = dynamic_cast<const Leaf *>(next)->sym_;
                return;
            } else if (dynamic_cast<const InternalNode *>(next))
                current = dynamic_cast<const InternalNode *>(next);
            else
                throw std::logic_error("Assertion error: Illegal node type");
        }
    }

}  // namespace raman

#endif  // RAMAN_CODER_H
