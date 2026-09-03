#include "substitution_cipher.h"

#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>

int main() {

    // Monoalphabetic substitution key
    std::map<char, char> key = {
        {'A', 'Q'}, {'B', 'W'}, {'C', 'E'}, {'D', 'R'},
        {'E', 'T'}, {'F', 'Y'}, {'G', 'U'}, {'H', 'I'},
        {'I', 'O'}, {'J', 'P'}, {'K', 'A'}, {'L', 'S'},
        {'M', 'D'}, {'N', 'F'}, {'O', 'G'}, {'P', 'H'},
        {'Q', 'J'}, {'R', 'K'}, {'S', 'L'}, {'T', 'Z'},
        {'U', 'X'}, {'V', 'C'}, {'W', 'V'}, {'X', 'B'},
        {'Y', 'N'}, {'Z', 'M'}
    };

    // Validate key
    if (!validateKey(key)) {
        std::cerr << "Error: Invalid substitution key.\n";
        return 1;
    }

    // Read plaintext
    std::ifstream inputFile(
        "classical/substitution_cipher/plaintext.txt"
    );

    if (!inputFile.is_open()) {
        std::cerr << "Error: Could not open plaintext.txt\n";
        return 1;
    }

    std::stringstream buffer;
    buffer << inputFile.rdbuf();
    std::string plaintext = buffer.str();

    inputFile.close();

    if (plaintext.empty()) {
        std::cerr << "Error: plaintext.txt is empty.\n";
        return 1;
    }

    // Encrypt plaintext
    std::string ciphertext =
        applySubstitution(plaintext, key);

    // Display result
    std::cout << "=== Monoalphabetic Substitution Cipher ===\n";

    std::cout << "\nPlaintext:\n";
    std::cout << plaintext << "\n";

    std::cout << "\nCiphertext:\n";
    std::cout << ciphertext << "\n";

    // Save ciphertext
    std::ofstream outputFile(
        "classical/substitution_cipher/ciphertext.txt"
    );

    if (!outputFile.is_open()) {
        std::cerr << "Error: Could not create ciphertext.txt\n";
        return 1;
    }

    outputFile << ciphertext;
    outputFile.close();

    std::cout << "\nCiphertext saved successfully.\n";

    // Frequency analysis
    frequencyAnalysis(ciphertext);

    // Word frequency analysis
    wordFrequencyAnalysis(ciphertext);

    return 0;
}
