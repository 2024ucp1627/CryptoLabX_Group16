#include "cryptanalysis.h"

#include <cctype>
#include <iostream>

std::vector<int> getWordPattern(const std::string& word)
{
    std::map<char, int> patternMap;
    std::vector<int> pattern;

    int nextNumber = 0;

    for (char ch : word)
    {
        char letter = std::toupper(
            static_cast<unsigned char>(ch)
        );

        if (patternMap.find(letter) == patternMap.end())
        {
            patternMap[letter] = nextNumber;
            nextNumber++;
        }

        pattern.push_back(patternMap[letter]);
    }

    return pattern;
}


std::map<std::vector<int>, std::vector<std::string>>
pattern_analysis(const std::string& ciphertext)
{
    std::map<std::vector<int>, std::vector<std::string>> patterns;

    std::string word;

    for (char ch : ciphertext)
    {
        if (std::isalpha(static_cast<unsigned char>(ch)))
        {
            word += ch;
        }
        else if (!word.empty())
        {
            std::vector<int> pattern = getWordPattern(word);

            patterns[pattern].push_back(word);

            word.clear();
        }
    }

    // Process the final word.
    if (!word.empty())
    {
        std::vector<int> pattern = getWordPattern(word);

        patterns[pattern].push_back(word);
    }

    return patterns;
}


void display_partial_plaintext(
    const std::string& ciphertext,
    const std::map<char, char>& substitution)
{
    for (char ch : ciphertext)
    {
        if (std::isalpha(static_cast<unsigned char>(ch)))
        {
            char upper = std::toupper(
                static_cast<unsigned char>(ch)
            );

            auto it = substitution.find(upper);

            if (it != substitution.end())
            {
                std::cout << it->second;
            }
            else
            {
                std::cout << '_';
            }
        }
        else
        {
            std::cout << ch;
        }
    }

    std::cout << '\n';
}


bool test_substitution(
    char cipherLetter,
    char plainLetter,
    std::map<char, char>& substitution)
{
    cipherLetter = std::toupper(
        static_cast<unsigned char>(cipherLetter)
    );

    plainLetter = std::toupper(
        static_cast<unsigned char>(plainLetter)
    );

    // Cipher letter already has a mapping.
    if (substitution.find(cipherLetter) != substitution.end())
    {
        return substitution[cipherLetter] == plainLetter;
    }

    // Plaintext letter is already assigned to another
    // ciphertext letter.
    for (const auto& entry : substitution)
    {
        if (entry.second == plainLetter)
        {
            return false;
        }
    }

    substitution[cipherLetter] = plainLetter;

    return true;
}


void iterative_cryptanalysis(const std::string& ciphertext)
{
    std::map<char, char> substitution;

    std::cout << "\n=== ITERATIVE CRYPTANALYSIS ===\n";

    std::cout << "\nInitial partial plaintext:\n";
    display_partial_plaintext(ciphertext, substitution);

    while (true)
    {
        char cipherLetter;
        char plainLetter;

        std::cout << "\nEnter ciphertext letter "
                     "(0 to finish): ";

        std::cin >> cipherLetter;

        cipherLetter = std::toupper(
            static_cast<unsigned char>(cipherLetter)
        );

        if (cipherLetter == '0')
        {
            break;
        }

        if (!std::isalpha(
                static_cast<unsigned char>(cipherLetter)))
        {
            std::cout << "Invalid ciphertext letter.\n";
            continue;
        }

        std::cout << "Enter proposed plaintext letter: ";

        std::cin >> plainLetter;

        plainLetter = std::toupper(
            static_cast<unsigned char>(plainLetter)
        );

        if (!std::isalpha(
                static_cast<unsigned char>(plainLetter)))
        {
            std::cout << "Invalid plaintext letter.\n";
            continue;
        }

        std::map<char, char> candidate = substitution;

        if (test_substitution(
                cipherLetter,
                plainLetter,
                candidate))
        {
            substitution = candidate;

            std::cout << "\nACCEPTED: "
                      << cipherLetter
                      << " -> "
                      << plainLetter
                      << "\n";

            std::cout << "\nUpdated partial plaintext:\n";

            display_partial_plaintext(
                ciphertext,
                substitution
            );
        }
        else
        {
            std::cout << "\nREJECTED: "
                      << cipherLetter
                      << " -> "
                      << plainLetter
                      << "\n";

            std::cout << "The substitution conflicts "
                         "with the current mapping.\n";
        }
    }

    std::cout << "\n=== FINAL PARTIAL PLAINTEXT ===\n";

    display_partial_plaintext(
        ciphertext,
        substitution
    );

    std::cout << "\n=== RECOVERED SUBSTITUTIONS ===\n";

    for (const auto& entry : substitution)
    {
        std::cout << entry.first
                  << " -> "
                  << entry.second
                  << "\n";
    }
}

bool verify_solution(
    const std::string& plaintext,
    const std::string& ciphertext,
    const std::map<char, char>& substitution)
{
    std::string reencrypted;

    for (char ch : plaintext)
    {
        if (std::isalpha(static_cast<unsigned char>(ch)))
        {
            char letter = std::toupper(
                static_cast<unsigned char>(ch)
            );

            if (substitution.find(letter) == substitution.end())
            {
                return false;
            }

            reencrypted += substitution.at(letter);
        }
        else
        {
            reencrypted += ch;
        }
    }

    return reencrypted == ciphertext;
}

void display_word_patterns(const std::string& ciphertext)
{
    std::map<std::string, std::vector<int>> wordPatterns;
    
    std::string word;

    for (char ch : ciphertext)
    {
        if (std::isalpha(static_cast<unsigned char>(ch)))
        {
            word += std::toupper(
                static_cast<unsigned char>(ch)
            );
        }
        else if (!word.empty())
        {
            wordPatterns[word] = getWordPattern(word);
            word.clear();
        }
    }

    if (!word.empty())
    {
        wordPatterns[word] = getWordPattern(word);
    }

    std::cout << "\n=== WORD PATTERNS ===\n\n";

    for (const auto& entry : wordPatterns)
    {
        std::cout << entry.first << " -> ";

        for (int number : entry.second)
        {
            std::cout << number << " ";
        }

        std::cout << "\n";
    }
}