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

            if (substitution.find(upper) != substitution.end())
            {
                std::cout << substitution.at(upper);
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

    char cipherLetter;
    char plainLetter;

    std::cout << "\n===== ITERATIVE CRYPTANALYSIS =====\n";

    while (true)
    {
        std::cout << "\nCurrent partial plaintext:\n";

        display_partial_plaintext(
            ciphertext,
            substitution
        );

        std::cout << "\nEnter ciphertext letter (0 to finish): ";
        std::cin >> cipherLetter;

        cipherLetter = std::toupper(
            static_cast<unsigned char>(cipherLetter)
        );

        if (cipherLetter == '0')
        {
            break;
        }

        std::cout << "Enter proposed plaintext letter: ";
        std::cin >> plainLetter;

        plainLetter = std::toupper(
            static_cast<unsigned char>(plainLetter)
        );

        if (test_substitution(
                cipherLetter,
                plainLetter,
                substitution))
        {
            std::cout << "Substitution ACCEPTED: "
                      << cipherLetter << " -> "
                      << plainLetter << "\n";
        }
        else
        {
            std::cout << "Substitution REJECTED: "
                      << cipherLetter << " -> "
                      << plainLetter << "\n";
        }
    }

    std::cout << "\nFinal partial plaintext:\n";

    display_partial_plaintext(
        ciphertext,
        substitution
    );
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