#include "substitution_cipher.h"

#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>

int main() {

    std::map<char, char> key = {
        {'A', 'Q'}, {'B', 'W'}, {'C', 'E'}, {'D', 'R'},
        {'E', 'T'}, {'F', 'Y'}, {'G', 'U'}, {'H', 'I'},
        {'I', 'O'}, {'J', 'P'}, {'K', 'A'}, {'L', 'S'},
        {'M', 'D'}, {'N', 'F'}, {'O', 'G'}, {'P', 'H'},
        {'Q', 'J'}, {'R', 'K'}, {'S', 'L'}, {'T', 'Z'},
        {'U', 'X'}, {'V', 'C'}, {'W', 'V'}, {'X', 'B'},
        {'Y', 'N'}, {'Z', 'M'}
    };

    if (!validateKey(key)) {
        std::cerr << "Error: Invalid substitution key.\n";
        return 1;
    }

    // Read plaintext from file.
    std::ifstream inputFile("classical/substitution_cipher/plaintext.txt");

    if (!inputFile.is_open()) {
        std::cerr << "Error: Could not open plaintext.txt\n";
        return 1;
    }

    std::stringstream buffer;
    buffer << inputFile.rdbuf();
    std::string plaintext = buffer.str();

    inputFile.close();

    std::cout << "=== Monoalphabetic Substitution Cipher ===\n";

    std::cout << "\nPlaintext:\n";
    std::cout << plaintext << "\n";

    std::string ciphertext =
        applySubstitution(plaintext, key);

    std::cout << "\nCiphertext:\n";
    std::cout << ciphertext << "\n";

    frequencyAnalysis(ciphertext);

    wordFrequencyAnalysis(ciphertext);

    return 0;
}
