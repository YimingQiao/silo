//
// Created by yiqiao on 11/17/2022.
//

#include <algorithm>
#include <cassert>
#include <stdexcept>
#include <utility>

#include "frequency_table.h"

namespace raman {
    uint32_t FreqStat::getSymbolLimit() const { return static_cast<uint32_t>(freq_.size()); }

    uint32_t FreqStat::Get(std::string &symbol) {
        size_t idx = Str2Idx(symbol);
        return freq_.at(idx);
    }

    void FreqStat::Set(std::string &str, uint32_t freq) {
        size_t idx = Str2Idx(str);
        freq_.at(idx) = freq;
    }

    void FreqStat::Increment(std::string &str) {
        size_t idx = Str2Idx(str);
        if (freq_[idx] == UINT32_MAX) throw std::overflow_error("Maximum frequency reached");
        freq_[idx] += 1;
    }

    CodeTree FreqStat::BuildCodeTree() const {
        // Note that if two nodes have the same frequency, then the tie is broken
        // by which tree contains the lowest symbol. Thus the algorithm has a
        // deterministic output and does not rely on the queue to break ties.
        std::priority_queue <NodeWithFrequency> pqueue;

        // Add leaves for symbols with non-zero frequency
        {
            uint32_t i = 0;
            for (uint32_t freq: freq_) {
                if (freq > 0) pqueue.push(NodeWithFrequency(new Leaf(i), i, freq));
                i++;
            }
        }

        // Pad with zero-frequency symbols until queue has at least 2 items
        {
            uint32_t i = 0;
            for (uint32_t freq: freq_) {
                if (pqueue.size() >= 2) break;
                if (freq == 0) pqueue.push(NodeWithFrequency(new Leaf(i), i, freq));
                i++;
            }
        }
        assert(pqueue.size() >= 2);

        // Repeatedly tie together two nodes with the lowest frequency
        while (pqueue.size() > 1) {
            NodeWithFrequency x = popQueue(pqueue);
            NodeWithFrequency y = popQueue(pqueue);
            pqueue.push(NodeWithFrequency(new InternalNode(std::move(x.node), std::move(y.node)),
                                          std::min(x.lowestSymbol, y.lowestSymbol),
                                          x.frequency + y.frequency));
        }

        // Return the remaining node
        NodeWithFrequency temp = popQueue(pqueue);
        InternalNode *root = dynamic_cast<InternalNode *>(temp.node.release());
        CodeTree result(std::move(*root), getSymbolLimit());
        delete root;
        return result;
    }

    FreqStat::NodeWithFrequency::NodeWithFrequency(Node *nd, uint32_t lowSym, uint64_t freq)
            : node(std::unique_ptr<Node>(nd)), lowestSymbol(lowSym), frequency(freq) {}

    bool FreqStat::NodeWithFrequency::operator<(const NodeWithFrequency &other) const {
        if (frequency > other.frequency)
            return true;
        else if (frequency < other.frequency)
            return false;
        else if (lowestSymbol > other.lowestSymbol)
            return true;
        else if (lowestSymbol < other.lowestSymbol)
            return false;
        else
            return false;
    }

    FreqStat::NodeWithFrequency FreqStat::popQueue(std::priority_queue <NodeWithFrequency> &pqueue) {
        FreqStat::NodeWithFrequency result = std::move(const_cast<NodeWithFrequency &&>(pqueue.top()));
        pqueue.pop();
        return result;
    }
}  // namespace raman