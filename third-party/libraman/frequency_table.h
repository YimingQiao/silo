#ifndef RAMAN_FREQUENCY_TABLE_H
#define RAMAN_FREQUENCY_TABLE_H

#include <cstdint>
#include <queue>
#include <unordered_map>
#include <vector>
#include <string>

#include "code_tree.h"

namespace raman {

// BiMap for Enum
    struct BiMap {
        std::vector <std::string> enums_;
        std::unordered_map <std::string, uint32_t> enum2idx_;
    };

    class FreqStat final {
    private:
        std::vector <std::uint32_t> freq_;
        BiMap bimap_;

    public:
        FreqStat() {
            std::string str;
            str.push_back('-');
            Str2Idx(str);
        }

    public:
        // Get Bimap Size.
        uint32_t BimapSize() const {
            uint32_t ret = 0;
            for (auto &str: bimap_.enums_) ret += str.size();

            return ret;
        }

    public:
        std::uint32_t getSymbolLimit() const;

        // Returns the frequency of the given symbol in this frequency table.
    public:
        std::uint32_t Get(std::string &symbol);

        // Sets the frequency of the given symbol in this frequency table to the given value.
    public:
        void Set(std::string &str, std::uint32_t freq);

        // Increments the frequency of the given symbol in this frequency table.
    public:
        void Increment(std::string &str);

        size_t Str2Idx(std::string &str) {
            auto it = bimap_.enum2idx_.find(str);
            if (it != bimap_.enum2idx_.end())
                return it->second;
            else {
                bimap_.enum2idx_[str] = bimap_.enums_.size();
                bimap_.enums_.push_back(str);
                freq_.push_back(0);
                return bimap_.enums_.size() - 1;
            }
        }

        std::string &Idx2Str(size_t idx) { return bimap_.enums_[idx]; }

        /*---- Advanced methods ----*/

        // Returns a code tree that is optimal for the symbol frequencies in this table.
        // The tree always contains at least 2 leaves (even if they come from symbols with
        // 0 frequency), to avoid degenerate trees. Note that optimal trees are not unique.
    public:
        CodeTree BuildCodeTree() const;

        // Helper structure for buildCodeTree()
    private:
        class NodeWithFrequency {
        public:
            std::unique_ptr <Node> node;

        public:
            std::uint32_t lowestSymbol;

        public:
            std::uint64_t frequency;  // Using wider type prevents overflow

        public:
            explicit NodeWithFrequency(Node *nd, std::uint32_t lowSym, std::uint64_t freq);

            // Sort by ascending frequency, breaking ties by ascending symbol value.
        public:
            bool operator<(const NodeWithFrequency &other) const;
        };

    private:
        static NodeWithFrequency popQueue(std::priority_queue <NodeWithFrequency> &pqueue);
    };

}  // namespace raman

#endif  // RAMAN_FREQUENCY_TABLE_H
