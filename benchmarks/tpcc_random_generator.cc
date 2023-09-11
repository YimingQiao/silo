#include "tpcc_random_generator.h"

#include <cstdio>
#include <cstring>

TPCCRandomGenerator::TPCCRandomGenerator(fast_random &r) : r_(r) {
  loadCorpus();
  std::cerr << "Corpus Loaded.\n";
  loadDataDist();
  std::cerr << "Numeric Distribution Loaded.\n";
}

void TPCCRandomGenerator::HistoryData(char *s, int upper_length) { wordsData(upper_length, 3); }

void TPCCRandomGenerator::CustomerData(char *s, int upper_length, bool bad_credit) {
  int32_t word_num = 10;
  std::vector<int> word_idx(word_num);
  int total_length = upper_length + 1;
  while (total_length > upper_length) {
    total_length = word_num - 1;
    for (int i = 0; i < word_num; i++) {
      word_idx[i] = RandomNumber(0, stock_data_corpus_.size() - 1);
      total_length += stock_data_corpus_[word_idx[i]].size();
    }
  }
  for (int i = 0; i < word_num; i++) {
    std::string &word = stock_data_corpus_[word_idx[i]];
    strncpy(s, word.c_str(), word.size());

    s += word.size();
    if (i != word_num - 1) {
      *s = ' ';
      s++;
    }
  }
  *s = '\0';

  // Bad credit: insert history into c_data
  if (bad_credit) {
    static const int HISTORY_SIZE = 30;
    char history[HISTORY_SIZE];
    int record_num = RandomNumber(1, 5);
    for (int i = 0; i < record_num; ++i) {
      int characters =
          snprintf(history, HISTORY_SIZE, " %04d-%02d-%03d-%02d-%03d-%04d", RandomNumber(1, 3000), RandomNumber(1, 10),
                   RandomNumber(1, 100), RandomNumber(1, 10), RandomNumber(1, 100), RandomNumber(1, 10000));
      if (total_length + HISTORY_SIZE < upper_length) {
        strncpy(s, history, characters);
        s += characters;
        *s = '\0';
        total_length += characters;
      }
    }
  }
}

void TPCCRandomGenerator::PhoneData(char *s, int length) {
  if (length == 16) {
    memcpy(s, "+01-", 4);
    std::string &word = phone_district_code[RandomNumber(0, phone_district_code.size() - 1)];
    memcpy(s + 4, word.c_str(), 3);
    s[7] = '-';
    RandomString(s + 8, 3, 3);
    s[11] = '-';
    RandomString(s + 12, 4, 4);
  }
}

void TPCCRandomGenerator::DepartmentData(char *s, int upper_length) {
  if (upper_length > 13) {
    memcpy(s, "Department#", 11);
    RandomString(s + 11, 1, 2);
  }
}

void TPCCRandomGenerator::CustomerString(char *s, int upper_length, const std::string &corpus_name) {
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
    return;
  }

  std::string &word = (*corpus)[RandomNumber(0, corpus->size() - 1)];
  while (word.length() > upper_length) word = (*corpus)[RandomNumber(0, corpus->size() - 1)];
  strncpy(s, word.c_str(), word.size());
  s[word.size()] = '\0';
}

uint32_t TPCCRandomGenerator::CustomerIntDist(const std::string &name) {
  if (name == "payment_cnt") return cus_payment_cnt_dist_[RandomNumber(0, cus_payment_cnt_dist_.size() - 1)];
  else if (name == "delivery_cnt")
    return cus_delivery_cnt_dist_[RandomNumber(0, cus_delivery_cnt_dist_.size() - 1)];
  else { printf("Customer num dist name %s is not supported\n", name.c_str()); }
  return 0;
}

float TPCCRandomGenerator::CustomerFloatDist(const std::string &name) {
  if (name == "balance") return cus_balance_dist_[RandomNumber(0, cus_balance_dist_.size() - 1)];
  else if (name == "ytd_payment")
    return cus_ytd_payment_dist_[RandomNumber(0, cus_ytd_payment_dist_.size() - 1)];
  else { printf("Customer float dist name %s is not supported\n", name.c_str()); }
  return 0;
}

void TPCCRandomGenerator::loadCorpus() {
  if (!loadStockDataCorpus()) { printf("Loaded stock_data_corpus.txt failed\n"); }
  if (!loadFirstNames()) { printf("Loaded first_names.txt failed\n"); }
  if (!loadZip()) { printf("Loaded zip.txt failed\n"); }
  if (!loadStreet()) { printf("Loaded street.txt failed\n"); }
}

bool TPCCRandomGenerator::loadStockDataCorpus() {
  std::ifstream in("corpus/stock_data_corpus.txt");
  if (in.fail()) {
    printf("Failed to open stock_data_corpus.txt\n");
    return false;
  }

  std::string line;
  while (std::getline(in, line)) {
    if (line.back() == '\r') line.pop_back();
    stock_data_corpus_.push_back(line);
  }
  in.close();
  return true;
}

bool TPCCRandomGenerator::loadFirstNames() {
  std::ifstream in("corpus/first_names.txt");
  if (in.fail()) {
    printf("Failed to open first_names.txt\n");
    return false;
  }

  std::string line;
  while (std::getline(in, line)) {
    if (line.back() == '\r') line.pop_back();
    first_names_.push_back(line);
  }
  in.close();
  return true;
}

bool TPCCRandomGenerator::loadZip() {
  std::ifstream in("corpus/zip_corpus.txt");
  if (in.fail()) {
    printf("Failed to open zip.txt\n");
    return false;
  }

  std::string line;
  while (std::getline(in, line)) {
    if (line.back() == '\r') line.pop_back();
    const int32_t zip_length = 5;
    const int32_t state_length = 2;
    zip_.push_back(line.substr(0, zip_length));
    state_.push_back(line.substr(line.size() - state_length, state_length));
    city_.push_back(line.substr(zip_length + 1, line.size() - zip_length - state_length - 2));
  }
  in.close();
  return true;
}

bool TPCCRandomGenerator::loadStreet() {
  std::ifstream in("corpus/streets.txt");
  if (in.fail()) {
    printf("Failed to open street.txt\n");
    return false;
  }

  std::string line;
  while (std::getline(in, line)) {
    if (line.back() == '\r') line.pop_back();
    street_.push_back(line);
  }
  in.close();
  return true;
}

bool TPCCRandomGenerator::loadDataDist() {
  std::ifstream in("data_dist/stock_ytd_1m.txt");
  if (in.fail()) {
    printf("Failed to open stock_ytd_1m.txt\n");
    return false;
  }

  std::string line;
  while (std::getline(in, line)) {
    if (line.back() == '\r') line.pop_back();
    stock_ytd_dist_.push_back(std::stoi(line));
  }
  in.close();

  in.open("data_dist/stock_order_cnt_1m.txt");
  if (in.fail()) {
    printf("Failed to open stock_order_cnt_1m.txt\n");
    return false;
  }

  while (std::getline(in, line)) {
    if (line.back() == '\r') line.pop_back();
    stock_order_cnt_dist_.push_back(std::stoi(line));
  }
  in.close();

  in.open("data_dist/stock_remote_cnt_1m.txt");
  if (in.fail()) {
    printf("Failed to open stock_remote_cnt_1m.txt\n");
    return false;
  }

  while (std::getline(in, line)) {
    if (line.back() == '\r') line.pop_back();
    stock_remote_cnt_dist_.push_back(std::stoi(line));
  }
  in.close();

  in.open("data_dist/customer_delivery_cnt_1m.txt");
  if (in.fail()) {
    printf("Failed to open customer_delivery_cnt_1m.txt\n");
    return false;
  }

  while (std::getline(in, line)) {
    if (line.back() == '\r') line.pop_back();
    cus_delivery_cnt_dist_.push_back(std::stoi(line));
  }
  in.close();

  in.open("data_dist/customer_balance_1m.txt");
  if (in.fail()) {
    printf("Failed to open customer_balance_1m.txt\n");
    return false;
  }

  while (std::getline(in, line)) {
    if (line.back() == '\r') line.pop_back();
    cus_balance_dist_.push_back(std::stof(line));
  }
  in.close();

  in.open("data_dist/customer_ytd_payment_1m.txt");
  if (in.fail()) {
    printf("Failed to open customer_ytd_payment_1m.txt\n");
    return false;
  }

  while (std::getline(in, line)) {
    if (line.back() == '\r') line.pop_back();
    cus_ytd_payment_dist_.push_back(std::stof(line));
  }
  in.close();

  in.open("data_dist/customer_payment_cnt_1m.txt");
  if (in.fail()) {
    printf("Failed to open customer_payment_cnt_1m.txt\n");
    return false;
  }

  while (std::getline(in, line)) {
    if (line.back() == '\r') line.pop_back();
    cus_payment_cnt_dist_.push_back(std::stoi(line));
  }
  in.close();
  return true;
}
