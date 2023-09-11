#pragma once

#include <cstdlib>
#include <cstring>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

#include "../util.h"

using namespace util;

class TPCCRandomGenerator {
public:
  explicit TPCCRandomGenerator(fast_random &r);

public:
  inline ALWAYS_INLINE uint32_t StockIntDist(const std::string &name) {
    if (name == "ytd") return stock_ytd_dist_[RandomNumber(0, stock_ytd_dist_.size() - 1)];
    else if (name == "order_cnt")
      return stock_order_cnt_dist_[RandomNumber(0, stock_order_cnt_dist_.size() - 1)];
    else if (name == "remote_cnt")
      return stock_remote_cnt_dist_[RandomNumber(0, stock_remote_cnt_dist_.size() - 1)];
    else { printf("Stock num dist name %s is not supported\n", name.c_str()); }
    return 0;
  }

  inline ALWAYS_INLINE std::string StockData(int upper_length, bool is_original) {
    std::string s_data = wordsData(upper_length, 4);

    if (is_original) {
      int length = s_data.size();
      int position;
      for (position = length; position >= 0; position--) {
        if (s_data[position] == ' ') break;
      }
      s_data = s_data.substr(0, position + 1) + "original";
    }

    return s_data;
  }

  inline ALWAYS_INLINE std::string HistoryData(int upper_length) { return wordsData(upper_length, 3); }

  std::string CustomerData(int upper_length, bool bad_credit);

  inline ALWAYS_INLINE std::string PhoneData(int length) {
    if (length == 16) {
      std::string s("+01-");
      std::string &word = phone_district_code[RandomNumber(0, phone_district_code.size() - 1)];
      s += word + "-" + RandomString(3, 3) + "-" + RandomString(4, 4);
      return s;
    } else {
      std::cerr << "[TPCCRandomGenerator::PhoneData] length is not supported\n";
      return "";
    }
  }

  inline ALWAYS_INLINE std::string DepartmentData(int upper_length) {
    if (upper_length > 13) {
      std::string s = "Department#";
      return s + RandomString(1, 2);
    } else {
      std::cerr << "[TPCCRandomGenerator::DepartmentData] upper_length is too small (<= 13)\n";
    }
  }

  inline ALWAYS_INLINE std::string CustomerString(int upper_length, const std::string &corpus_name) {
    std::vector<std::string> *corpus;
    if (corpus_name == "first_name") {
      corpus = &first_names_;
    } else if (corpus_name == "street") {
      corpus = &street_;
    } else if (corpus_name == "city") {
      corpus = &city_;
    } else if (corpus_name == "state") {
      corpus = &state_;
    } else if (corpus_name == "zip") {
      corpus = &zip_;
    } else if (corpus_name == "stock_data") {
      corpus = &stock_data_corpus_;
    } else {
      printf("Corpus name %s is not supported\n", corpus_name.c_str());
      return "";
    }

    std::string &words = (*corpus)[RandomNumber(0, corpus->size() - 1)];
    while (words.length() > upper_length) words = (*corpus)[RandomNumber(0, corpus->size() - 1)];
    return words;
  }

  inline ALWAYS_INLINE uint32_t CustomerIntDist(const std::string &name) {
    if (name == "payment_cnt") return cus_payment_cnt_dist_[RandomNumber(0, cus_payment_cnt_dist_.size() - 1)];
    else if (name == "delivery_cnt")
      return cus_delivery_cnt_dist_[RandomNumber(0, cus_delivery_cnt_dist_.size() - 1)];
    else { printf("Customer num dist name %s is not supported\n", name.c_str()); }
    return 0;
  }

  inline ALWAYS_INLINE float CustomerFloatDist(const std::string &name) {
    if (name == "balance") return cus_balance_dist_[RandomNumber(0, cus_balance_dist_.size() - 1)];
    else if (name == "ytd_payment")
      return cus_ytd_payment_dist_[RandomNumber(0, cus_ytd_payment_dist_.size() - 1)];
    else { printf("Customer float dist name %s is not supported\n", name.c_str()); }
    return 0;
  }

  static inline ALWAYS_INLINE std::string DistInfo(int d_id, int w_id, int i_id) {
    std::vector<char> buffer(24 + 1);// +1 for the null terminator
    snprintf(buffer.data(), buffer.size(), "dist-info-str#%02d#%02d#%04d", d_id, w_id, i_id);
    return {buffer.data()};
  }

private:
  inline ALWAYS_INLINE int RandomNumber(int min, int max) { return r_.next_uniform() * (max - min + 1) + min; }

  inline ALWAYS_INLINE std::string RandomString(int lower, int upper, char base = '0', int num_characters = 10) {
    int length = RandomNumber(lower, upper);
    std::string s;
    s.resize(length);
    for (int i = 0; i < length; ++i) { s[i] = static_cast<char>(base + RandomNumber(0, num_characters - 1)); }
    return s;
  }

private:
  fast_random &r_;
  std::vector<std::string> stock_data_corpus_;
  std::vector<std::string> first_names_;
  std::vector<std::string> zip_;
  std::vector<std::string> city_;
  std::vector<std::string> state_;
  std::vector<std::string> street_;
  std::vector<std::string> phone_district_code = {
      "617", "508",       // Boston, MA
      "773", "312", "872",// Chicago, IL
      "214", "469", "972",// Dallas, TX
      "303", "720",       // Denver, CO
      "305", "786",       // Miami, FL
      "212", "646",       // New York, NY
      "267", "215",       // Philadelphia, PA
      "602", "480",       // Phoenix, AZ
      "503", "971",       // Portland, OR
      "901", "615", "423",// Memphis, TN
      "210", "512",       // San Antonio, TX
      "415", "650", "408",// San Francisco, CA
      "206", "425",       // Seattle, WA
      "703", "571",       // Washington, DC
  };

  std::vector<uint32_t> stock_ytd_dist_;
  std::vector<uint32_t> stock_order_cnt_dist_;
  std::vector<uint32_t> stock_remote_cnt_dist_;

  std::vector<uint32_t> cus_delivery_cnt_dist_;
  std::vector<float> cus_balance_dist_;
  std::vector<float> cus_ytd_payment_dist_;
  std::vector<uint32_t> cus_payment_cnt_dist_;

  inline ALWAYS_INLINE std::string wordsData(int upper_length, int num_word) {
    std::vector<int> word_idx(num_word);
    int total_length = upper_length + 1;
    while (total_length > upper_length) {
      total_length = num_word - 1;
      for (int i = 0; i < num_word; i++) {
        word_idx[i] = RandomNumber(0, stock_data_corpus_.size() - 1);
        total_length += stock_data_corpus_[word_idx[i]].size();
      }
    }

    std::string data;
    for (int i = 0; i < num_word; i++) {
      std::string &word = stock_data_corpus_[word_idx[i]];
      data += word;
      if (i != num_word - 1) { data += " "; }
    }

    return data;
  }

  void loadCorpus();
  bool loadStockDataCorpus();
  bool loadFirstNames();
  bool loadZip();
  bool loadStreet();
  bool loadDataDist();
};
