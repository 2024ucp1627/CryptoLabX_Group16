#include "substitution_cipher.h"

#include <algorithm>
#include <cctype>
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <vector>


// ---------------------------------------------------------
// Validate substitution key
// ---------------------------------------------------------
bool validateKey(const std::map<char, char>& key) {

    // A valid monoalphabetic substitution key
    // must contain exactly 26 mappings.
    if (key.size() != 26) {
        return false;
    }

    std::map<char, bool> used;

    for (const auto& entry : key) {

        char plain = entry.first;
        char cipher = entry.second;

        // Plaintext letter must be A-Z.
        if (plain < 'A' || plain > 'Z') {
            return false;
        }

        // Ciphertext letter must be A-Z.
        if (cipher < 'A' || cipher > 'Z') {
            return false;
        }

        // Ciphertext letters must be unique.
        if (used[cipher]) {
            return false;
        }

        used[cipher] = true;
    }

    return true;
}


// ---------------------------------------------------------
// Apply monoalphabetic substitution
// ---------------------------------------------------------
std::string applySubstitution(
    const std::string& text,
    const std::map<char, char>& key
) {
    std::string result;

    for (char ch : text) {

        char upperChar = static_cast<char>(
            std::toupper(static_cast<unsigned char>(ch))
        );

        auto it = key.find(upperChar);

        if (it != key.end()) {

            char substituted = it->second;

            // Preserve lowercase letters.
            if (std::islower(static_cast<unsigned char>(ch))) {

                substituted = static_cast<char>(
                    std::tolower(
                        static_cast<unsigned char>(substituted)
                    )
                );
            }

            result += substituted;

        } else {

            // Keep spaces, punctuation, numbers, etc.
            // unchanged.
            result += ch;
        }
    }

    return result;
}


// ---------------------------------------------------------
// Letter frequency analysis
// ---------------------------------------------------------
void frequencyAnalysis(const std::string& ciphertext) {

    std::map<char, int> frequency;

    int totalLetters = 0;

    // Count every alphabetic character.
    for (char ch : ciphertext) {

        if (std::isalpha(static_cast<unsigned char>(ch))) {

            char upperChar = static_cast<char>(
                std::toupper(static_cast<unsigned char>(ch))
            );

            frequency[upperChar]++;
            totalLetters++;
        }
    }

    // Convert map into vector for sorting.
    std::vector<std::pair<char, int>> frequencies(
        frequency.begin(),
        frequency.end()
    );

    // Sort from highest frequency to lowest.
    std::sort(
        frequencies.begin(),
        frequencies.end(),
        [](const auto& a, const auto& b) {

            return a.second > b.second;
        }
    );

    std::cout << "\n=== Letter Frequency Analysis ===\n";

    std::cout << std::left
              << std::setw(10) << "Letter"
              << std::setw(10) << "Count"
              << "Percentage\n";

    std::cout << "------------------------------\n";

    if (totalLetters == 0) {
        std::cout << "No alphabetic characters found.\n";
        return;
    }

    for (const auto& entry : frequencies) {

        double percentage =
            (static_cast<double>(entry.second)
             / totalLetters) * 100.0;

        std::cout << std::left
                  << std::setw(10) << entry.first
                  << std::setw(10) << entry.second
                  << std::fixed
                  << std::setprecision(2)
                  << percentage
                  << "%\n";
    }
}


// ---------------------------------------------------------
// Word frequency analysis
// ---------------------------------------------------------
void wordFrequencyAnalysis(const std::string& ciphertext) {

    std::map<std::string, int> wordFrequency;

    std::string currentWord;

    // Extract words from ciphertext.
    for (char ch : ciphertext) {

        if (std::isalpha(static_cast<unsigned char>(ch))) {

            currentWord += static_cast<char>(
                std::toupper(static_cast<unsigned char>(ch))
            );

        } else {

            if (!currentWord.empty()) {

                wordFrequency[currentWord]++;
                currentWord.clear();
            }
        }
    }

    // Handle the final word.
    if (!currentWord.empty()) {
        wordFrequency[currentWord]++;
    }


    // -----------------------------------------------------
    // One-letter words
    // -----------------------------------------------------
    std::cout << "\n=== One-Letter Words ===\n";

    bool foundOneLetter = false;

    for (const auto& entry : wordFrequency) {

        if (entry.first.length() == 1) {

            std::cout << entry.first
                      << " : "
                      << entry.second
                      << "\n";

            foundOneLetter = true;
        }
    }

    if (!foundOneLetter) {
        std::cout << "None\n";
    }


    // -----------------------------------------------------
    // Two-letter words
    // -----------------------------------------------------
    std::cout << "\n=== Two-Letter Words ===\n";

    bool foundTwoLetter = false;

    for (const auto& entry : wordFrequency) {

        if (entry.first.length() == 2) {

            std::cout << entry.first
                      << " : "
                      << entry.second
                      << "\n";

            foundTwoLetter = true;
        }
    }

    if (!foundTwoLetter) {
        std::cout << "None\n";
    }


    // -----------------------------------------------------
    // Three-letter words
    // -----------------------------------------------------
    std::cout << "\n=== Three-Letter Words ===\n";

    bool foundThreeLetter = false;

    for (const auto& entry : wordFrequency) {

        if (entry.first.length() == 3) {

            std::cout << entry.first
                      << " : "
                      << entry.second
                      << "\n";

            foundThreeLetter = true;
        }
    }

    if (!foundThreeLetter) {
        std::cout << "None\n";
    }


    // -----------------------------------------------------
    // Repeated words
    // -----------------------------------------------------
    std::cout << "\n=== Repeated Words ===\n";

    bool foundRepeated = false;

    for (const auto& entry : wordFrequency) {

        if (entry.second > 1) {

            std::cout << entry.first
                      << " : "
                      << entry.second
                      << "\n";

            foundRepeated = true;
        }
    }

    if (!foundRepeated) {
        std::cout << "None\n";
    }
}
