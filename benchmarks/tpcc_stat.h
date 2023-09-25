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

public:
    inline ALWAYS_INLINE void Insert(uint64_t size, bool is_mem, const std::string &table_name) {
        if (table_name != "order" && table_name != "new_order") {
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
        if (total_mem_ + size < total_mem_limit_) return;

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
        Insert(size, true, table_name);
    }

    inline ALWAYS_INLINE bool ToMemory(uint64_t size) const {
        return total_mem_limit_ > total_mem_ + size;
    }

private:
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
};
