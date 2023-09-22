#pragma once

#include "tpcc.h"

using vector_of_string = std::vector<std::string>;

static uint32_t GetWarehouseID(customer::key &key) { return key.c_w_id; }

static uint32_t GetWarehouseID(stock::key &key) { return key.s_w_id; }

static uint32_t GetWarehouseID(oorder::key &key) { return key.o_w_id; }

static uint32_t GetWarehouseID(order_line::key &key) { return key.ol_w_id; }

static uint32_t GetWarehouseID(history::key &key) { return key.h_w_id; }


// -------------------------- Helper: Tuple to Raman Format -------------------------------------
static vector_of_string ToRamanFormat(const stock::value &stock) {
    std::vector <std::string> ret{std::to_string(stock.s_quantity), std::to_string(stock.s_ytd),
                                  std::to_string(stock.s_order_cnt), std::to_string(stock.s_remote_cnt)};
    return std::move(ret);
}

static vector_of_string ToRamanFormat(const stock_data::value &stock_data) {
    std::vector <std::string> ret{stock_data.s_dist_01.str(), stock_data.s_dist_02.str(), stock_data.s_dist_03.str(),
                                  stock_data.s_dist_04.str(), stock_data.s_dist_05.str(), stock_data.s_dist_06.str(),
                                  stock_data.s_dist_07.str(), stock_data.s_dist_08.str(), stock_data.s_dist_09.str(),
                                  stock_data.s_dist_10.str(), stock_data.s_data.str()};
    return std::move(ret);
}

static vector_of_string ToRamanFormat(const order_line::value &orderline) {
    std::vector <std::string> ret{std::to_string(orderline.ol_quantity), std::to_string(orderline.ol_amount),
                                  std::to_string(orderline.ol_delivery_d), std::to_string(orderline.ol_i_id),
                                  std::to_string(orderline.ol_supply_w_id), orderline.ol_dist_info.str()};
    return std::move(ret);
}

static vector_of_string ToRamanFormat(const customer::value &customer) {
    std::vector <std::string> ret{std::to_string(customer.c_discount),
                                  customer.c_credit.str(),
                                  customer.c_last.str(),
                                  customer.c_first.str(),
                                  std::to_string(customer.c_credit_lim),
                                  std::to_string(customer.c_balance),
                                  std::to_string(customer.c_ytd_payment),
                                  std::to_string(customer.c_payment_cnt),
                                  std::to_string(customer.c_delivery_cnt),
                                  customer.c_street_1.str(),
                                  customer.c_street_2.str(),
                                  customer.c_city.str(),
                                  customer.c_state.str(),
                                  customer.c_zip.str(),
                                  customer.c_phone.str(),
                                  std::to_string(customer.c_since),
                                  customer.c_middle.str(),
                                  customer.c_data.str()};
    return std::move(ret);
}

static vector_of_string ToRamanFormat(const oorder::value &order) {
    std::vector <std::string> ret{std::to_string(order.o_c_id),
                                  std::to_string(order.o_carrier_id),
                                  std::to_string(order.o_ol_cnt),
                                  std::to_string(order.o_all_local),
                                  std::to_string(order.o_entry_d)};
    return std::move(ret);
}

static vector_of_string ToRamanFormat(const history::value &history) {
    std::vector <std::string> ret{std::to_string(history.h_amount), history.h_data.str()};
    return std::move(ret);
}

static void FromRamanFormat(vector_of_string &raman_sample, stock::value &stock) {
    stock.s_quantity = std::stoi(raman_sample[0]);
    stock.s_ytd = std::stoi(raman_sample[1]);
    stock.s_order_cnt = std::stoi(raman_sample[2]);
    stock.s_remote_cnt = std::stoi(raman_sample[3]);
}

static void FromRamanFormat(vector_of_string &sample, stock_data::value &stock) {
    stock.s_dist_01 = std::move(sample[0]);
    stock.s_dist_02 = std::move(sample[1]);
    stock.s_dist_03 = std::move(sample[2]);
    stock.s_dist_04 = std::move(sample[3]);
    stock.s_dist_05 = std::move(sample[4]);
    stock.s_dist_06 = std::move(sample[5]);
    stock.s_dist_07 = std::move(sample[6]);
    stock.s_dist_08 = std::move(sample[7]);
    stock.s_dist_09 = std::move(sample[8]);
    stock.s_dist_10 = std::move(sample[9]);
    stock.s_data = std::move(sample[10]);
}

static void FromRamanFormat(vector_of_string &sample, order_line::value &orderline) {
    orderline.ol_quantity = std::stoi(sample[0]);
    orderline.ol_amount = std::stoi(sample[1]);
    orderline.ol_delivery_d = std::stoi(sample[2]);
    orderline.ol_i_id = std::stoi(sample[3]);
    orderline.ol_supply_w_id = std::stoi(sample[4]);
    orderline.ol_dist_info = std::move(sample[5]);
}

static void FromRamanFormat(vector_of_string &sample, customer::value &customer) {
    customer.c_discount = std::stoi(sample[0]);
    customer.c_credit = std::move(sample[1]);
    customer.c_last = std::move(sample[2]);
    customer.c_first = std::move(sample[3]);
    customer.c_credit_lim = std::stoi(sample[4]);
    customer.c_balance = std::stoi(sample[5]);
    customer.c_ytd_payment = std::stoi(sample[6]);
    customer.c_payment_cnt = std::stoi(sample[7]);
    customer.c_delivery_cnt = std::stoi(sample[8]);
    customer.c_street_1 = std::move(sample[9]);
    customer.c_street_2 = std::move(sample[10]);
    customer.c_city = std::move(sample[11]);
    customer.c_state = std::move(sample[12]);
    customer.c_zip = std::move(sample[13]);
    customer.c_phone = std::move(sample[14]);
    customer.c_since = std::stoi(sample[15]);
    customer.c_middle = std::move(sample[16]);
    customer.c_data = std::move(sample[17]);
}

static void FromRamanFormat(vector_of_string &sample, oorder::value &order) {
    order.o_c_id = std::stoi(sample[0]);
    order.o_carrier_id = std::stoi(sample[1]);
    order.o_ol_cnt = std::stoi(sample[2]);
    order.o_all_local = std::stoi(sample[3]);
    order.o_entry_d = std::stoi(sample[4]);
}

static void FromRamanFormat(vector_of_string &sample, history::value &history) {
    history.h_amount = std::stoi(sample[0]);
    history.h_data = std::move(sample[1]);
}