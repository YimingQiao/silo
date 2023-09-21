#include "code_tree.h"

namespace raman {
    Node::~Node() = default;

    Leaf::Leaf(uint32_t sym) : sym_(sym) {}

    InternalNode::InternalNode(std::unique_ptr <Node> &&left, std::unique_ptr <Node> &&right)
            : l_(std::move(left)), r_(std::move(right)) {}

    CodeTree::CodeTree(InternalNode &&rt, uint32_t symbolLimit) : root_(std::move(rt)) {
        if (symbolLimit < 2) throw std::domain_error("At least 2 symbols needed");
        codes_ =
                std::vector < std::vector < bool > > (symbolLimit, std::vector<bool>());  // Initially all empty
        std::vector<bool> prefix;
        BuildCodeList(&root_, prefix);  // Fill 'codes' with appropriate data
    }

    void CodeTree::BuildCodeList(const Node *node, std::vector<bool> &prefix) {
        if (dynamic_cast<const InternalNode *>(node) != nullptr) {
            const InternalNode *internal = dynamic_cast<const InternalNode *>(node);

            prefix.push_back(0);
            BuildCodeList(internal->l_.get(), prefix);
            prefix.pop_back();

            prefix.push_back(1);
            BuildCodeList(internal->r_.get(), prefix);
            prefix.pop_back();

        } else if (dynamic_cast<const Leaf *>(node) != nullptr) {
            const Leaf *leaf = dynamic_cast<const Leaf *>(node);
            if (leaf->sym_ >= codes_.size()) throw std::invalid_argument("Symbol exceeds symbol limit");
            if (!codes_.at(leaf->sym_).empty())
                throw std::invalid_argument("Symbol has more than one code");
            codes_.at(leaf->sym_) = prefix;

        } else {
            throw std::logic_error("Assertion error: Illegal node type");
        }
    }

    const std::vector<bool> &CodeTree::GetCode(uint32_t symbol) const {
        if (codes_.at(symbol).empty())
            throw std::domain_error("No code for given symbol");
        else
            return codes_.at(symbol);
    }
}  // namespace raman