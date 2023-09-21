#ifndef RAMAN_CODE_TREE_H
#define RAMAN_CODE_TREE_H

#include <cstdint>
#include <memory>
#include <stdexcept>
#include <utility>
#include <vector>

namespace raman {
/*
 * A node in a code tree. This class has exactly two subclasses: InternalNode, Leaf.
 */
    class Node {
    public:
        virtual ~Node() = 0;
    };

/*
 * A leaf node in a code tree. It has a symbol value.
 */
    class Leaf final : public Node {
    public:
        std::uint32_t sym_;

    public:
        explicit Leaf(std::uint32_t sym);
    };

/*
 * An internal node in a code tree. It has two nodes as children.
 */
    class InternalNode final : public Node {
    public:
        std::unique_ptr <Node> l_;  // Not null
        std::unique_ptr <Node> r_;  // Not null

        explicit InternalNode(std::unique_ptr <Node> &&left, std::unique_ptr <Node> &&right);
    };

    class CodeTree final {
        /*---- Fields ----*/

    public:

        InternalNode root_;

    private:
        std::vector <std::vector<bool>> codes_;

    public:
        explicit CodeTree(InternalNode &&rt, std::uint32_t symbolLimit);

        /*---- Methods ----*/

        // Recursive helper function for the constructor
    private:
        void BuildCodeList(const Node *node, std::vector<bool> &prefix);

        // Returns the Huffman code for the given symbol, which is a list of 0s and 1s.
    public:
        const std::vector<bool> &GetCode(std::uint32_t symbol) const;

    public:
        // Return size in **byte**.
        uint32_t Size() const {
            uint32_t ret = 0;
            for (const auto &code: codes_) {
                ret += code.size();
            }

            return ret >> 3;
        }
    };
}  // namespace raman

#endif  // RAMAN_CODE_TREE_H
