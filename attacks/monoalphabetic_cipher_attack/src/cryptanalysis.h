#ifndef CRYPTANALYSIS_H
#define CRYPTANALYSIS_H

#include <string>
#include <vector>
#include <map>

std::vector<int> getWordPattern(const std::string& word);

std::map<std::vector<int>, std::vector<std::string>>
pattern_analysis(const std::string& ciphertext);

void display_partial_plaintext(
    const std::string& ciphertext,
    const std::map<char, char>& substitution
);

bool test_substitution(
    char cipherLetter,
    char plainLetter,
    std::map<char, char>& substitution
);

void iterative_cryptanalysis(const std::string& ciphertext);

bool verify_solution(
    const std::string& plaintext,
    const std::string& ciphertext,
    const std::map<char, char>& substitution
);

#endif