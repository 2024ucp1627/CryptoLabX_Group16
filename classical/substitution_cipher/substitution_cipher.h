#ifndef SUBSTITUTION_CIPHER_H
#define SUBSTITUTION_CIPHER_H

#include <string>
#include <map>
#include <vector>

std::string applySubstitution(
    const std::string& text,
    const std::map<char, char>& key
);

bool validateKey(const std::map<char, char>& key);

void frequencyAnalysis(const std::string& ciphertext);

void wordFrequencyAnalysis(const std::string& ciphertext);

#endif
