#pragma once

#include <cstdint>
#include <string>

#include "../macros.h"

class TPCCStat {
public:
    const int32_t kPageSize = 4096;

    explicit TPCCStat(uint64_t total_mem_limit) : total_mem_limit_(total_mem_limit) {}

    uint64_t n_c_mem = 0;
    uint64_t n_c_disk = 0;

    uint64_t n_h_mem = 0;
    uint64_t n_h_disk = 0;

    uint64_t n_ol_mem = 0;
    uint64_t n_ol_disk = 0;

    uint64_t n_s_mem = 0;
    uint64_t n_s_disk = 0;

    uint64_t warehouse_mem_ = 0;
    uint64_t warehouse_disk_ = 0;

    uint64_t district_mem_ = 0;
    uint64_t district_disk_ = 0;

    uint64_t customer_mem_ = 0;
    uint64_t customer_disk_ = 0;

    uint64_t history_mem_ = 0;
    uint64_t history_disk_ = 0;

    uint64_t order_mem_ = 0;
    uint64_t order_disk_ = 0;

    uint64_t new_order_mem_ = 0;
    uint64_t new_order_disk_ = 0;

    uint64_t order_line_mem_ = 0;
    uint64_t order_line_disk_ = 0;

    uint64_t item_mem_ = 0;
    uint64_t item_disk_ = 0;

    uint64_t stock_mem_ = 0;
    uint64_t stock_disk_ = 0;

    uint64_t total_mem_ = 0;
    uint64_t total_disk_ = 0;

    uint64_t total_mem_limit_;

public:
    inline ALWAYS_INLINE void Insert(uint64_t size, bool is_mem, const std::string &table_name) {
        if (table_name != "order" && table_name != "new_order" && table_name != "history") {
            if (is_mem) total_mem_ += size;
            else total_disk_ += size;
        }

        if (table_name == "warehouse") {
            if (is_mem) warehouse_mem_ += size;
            else warehouse_disk_ += size;
        } else if (table_name == "district") {
            if (is_mem) district_mem_ += size;
            else district_disk_ += size;
        } else if (table_name == "customer") {
            if (is_mem) customer_mem_ += size;
            else customer_disk_ += size;
        } else if (table_name == "history") {
            if (is_mem) history_mem_ += size;
            else history_disk_ += size;
        } else if (table_name == "order") {
            if (is_mem) order_mem_ += size;
            else order_disk_ += size;
        } else if (table_name == "new_order") {
            if (is_mem) new_order_mem_ += size;
            else new_order_disk_ += size;
        } else if (table_name == "order_line") {
            if (is_mem) order_line_mem_ += size;
            else order_line_disk_ += size;
        } else if (table_name == "item") {
            if (is_mem) item_mem_ += size;
            else item_disk_ += size;
        } else if (table_name == "stock") {
            if (is_mem) stock_mem_ += size;
            else stock_disk_ += size;
        } else {
            printf("Error: table name not found!\n");
        }
    }

    inline ALWAYS_INLINE void SwapTuple(uint64_t size, const std::string &table_name) {
        Insert(size, true, table_name);

        while (total_mem_ + size > total_mem_limit_) {
            total_mem_ -= kPageSize;
            total_disk_ += kPageSize;

            if (table_name == "stock") {
                stock_mem_ -= kPageSize;
                stock_disk_ += kPageSize;
            } else if (table_name == "customer") {
                customer_mem_ -= kPageSize;
                customer_disk_ += kPageSize;
            } else if (table_name == "order_line") {
                order_line_mem_ -= kPageSize;
                order_line_disk_ += kPageSize;
            } else
                printf("Error: table name not found!\n");
        }
    }

    inline ALWAYS_INLINE bool ToMemory(uint64_t size) const {
        return total_mem_limit_ > total_mem_ + size;
    }

    void Print(bool detailed = false) {
        if (detailed) {
            std::cerr << "[Table Name]: " << "[Memory Size] + [Disk Size]" << std::endl;
            std::cerr << "Warehouse: " << warehouse_mem_ << " byte" << std::endl;
            std::cerr << "District: " << district_mem_ << " byte" << std::endl;
            std::cerr << "Customer: " << customer_mem_ << " + " << customer_disk_ << " byte"
                      << std::endl;
            std::cerr << "Order: " << order_mem_ << " byte" << std::endl;
            std::cerr << "Order_line: " << order_line_mem_ << " + " << order_line_disk_
                      << " byte" << std::endl;
            std::cerr << "New_order: " << new_order_mem_ << " byte" << std::endl;
            std::cerr << "Item: " << item_mem_ << " byte" << std::endl;
            std::cerr << "Stock: " << stock_mem_ << " + " << stock_disk_ << " byte"
                      << std::endl;
            std::cerr << "History: " << history_mem_ << " byte" << std::endl;
            std::cerr << "--------------------------------------------" << std::endl;
        }
        uint64_t mem_total = warehouse_mem_ + district_mem_ + customer_mem_ +
                             order_line_mem_ + item_mem_ + stock_mem_;
        uint64_t disk_total = customer_disk_ + order_line_disk_ + stock_disk_;
        uint64_t others = history_mem_ + new_order_mem_ + order_mem_;
        std::cerr << "Mem: " << double(mem_total) / (1 << 20) << " MB\t" << "Disk: " << double(disk_total) / (1 << 20)
                  << " MB\t" << "Other: " << double(others) / (1 << 20) << " MB" << std::endl;
        std::cerr << "-----------------------------------------------------\n";
    }
};
