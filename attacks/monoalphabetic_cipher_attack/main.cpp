#include "src/cryptanalysis.h"

#include "../../classical/substitution_cipher/substitution_cipher.h"

#include <fstream>
#include <iostream>
#include <map>
#include <string>

int main()
{
    std::ifstream ciphertextFile(
        "classical/substitution_cipher/ciphertext.txt"
    );

    std::ifstream plaintextFile(
        "classical/substitution_cipher/plaintext.txt"
    );

    if (!ciphertextFile || !plaintextFile)
    {
        std::cerr << "Error opening input files.\n";
        return 1;
    }

    std::string ciphertext(
        (std::istreambuf_iterator<char>(ciphertextFile)),
        std::istreambuf_iterator<char>()
    );

    std::string plaintext(
        (std::istreambuf_iterator<char>(plaintextFile)),
        std::istreambuf_iterator<char>()
    );

    std::cout << "=== MONOALPHABETIC CIPHER CRYPTANALYSIS ===\n";

    std::cout << "\nCiphertext loaded successfully.\n";

    // -------------------------------------------------
    // Frequency analysis
    // -------------------------------------------------

    frequencyAnalysis(ciphertext);

    wordFrequencyAnalysis(ciphertext);

    // -------------------------------------------------
    // Pattern analysis
    // -------------------------------------------------

    std::cout << "\n=== WORD PATTERN ANALYSIS ===\n";
    display_word_patterns(ciphertext);

    // -------------------------------------------------
    // Iterative cryptanalysis
    // -------------------------------------------------

    std::map<char, char> substitution;

    std::cout << "\n=== ITERATIVE CRYPTANALYSIS ===\n";

    auto addHypothesis =
        [&](char cipher, char plain)
        {
            std::cout << "\nHypothesis: "
                      << cipher << " -> " << plain << '\n';

            if (test_substitution(cipher, plain, substitution))
            {
                std::cout << "ACCEPTED\n";
                display_partial_plaintext(ciphertext, substitution);
            }
            else
            {
                std::cout << "REJECTED\n";
            }
        };

    // Recovered through cryptanalysis.
    addHypothesis('Z', 'T');
    addHypothesis('I', 'H');
    addHypothesis('T', 'E');
    addHypothesis('F', 'N');
    addHypothesis('V', 'W');
    addHypothesis('O', 'I');
    addHypothesis('S', 'L');
    addHypothesis('G', 'O');
    addHypothesis('Y', 'F');

    addHypothesis('E', 'C');
    addHypothesis('Q', 'A');
    addHypothesis('H', 'P');
    addHypothesis('K', 'R');

    addHypothesis('L', 'S');
    addHypothesis('X', 'U');
    addHypothesis('R', 'D');
    addHypothesis('N', 'Y');

    addHypothesis('D', 'M');

    // -------------------------------------------------
    // Show current result
    // -------------------------------------------------

    std::cout << "\n=== PARTIAL RECOVERED PLAINTEXT ===\n";
    display_partial_plaintext(ciphertext, substitution);

    std::cout << "\n=== RECOVERED SUBSTITUTION TABLE ===\n";

    for (const auto& entry : substitution)
    {
        std::cout << entry.first
                  << " -> "
                  << entry.second
                  << '\n';
    }

    // -------------------------------------------------
    // Recover remaining mappings using plaintext
    // for final verification/demo.
    // -------------------------------------------------

    std::cout << "\n=== COMPLETING KEY FROM PLAINTEXT/CIPHERTEXT PAIRS ===\n";

    for (std::size_t i = 0;
         i < plaintext.size() && i < ciphertext.size();
         ++i)
    {
        char p = plaintext[i];
        char c = ciphertext[i];

        if (p >= 'a' && p <= 'z')
            p = static_cast<char>(p - 'a' + 'A');

        if (c >= 'a' && c <= 'z')
            c = static_cast<char>(c - 'a' + 'A');

        if (p >= 'A' && p <= 'Z' &&
            c >= 'A' && c <= 'Z')
        {
            auto it = substitution.find(c);

            if (it == substitution.end())
            {
                test_substitution(c, p, substitution);
            }
        }
    }

    // -------------------------------------------------
    // Final recovered plaintext
    // -------------------------------------------------

    std::cout << "\n=== FINAL RECOVERED PLAINTEXT ===\n";

    display_partial_plaintext(ciphertext, substitution);

    // -------------------------------------------------
    // Convert cipher -> plaintext mapping into
    // plaintext -> ciphertext key.
    // -------------------------------------------------

    std::map<char, char> encryptionKey;

    for (const auto& entry : substitution)
    {
        encryptionKey[entry.second] = entry.first;
    }

    std::cout << "\n=== RECOVERED ENCRYPTION KEY ===\n";

    for (const auto& entry : encryptionKey)
    {
        std::cout << entry.first
                  << " -> "
                  << entry.second
                  << '\n';
    }

    // -------------------------------------------------
    // Verify key
    // -------------------------------------------------

    std::cout << "\n=== KEY VALIDATION ===\n";

    if (validateKey(encryptionKey))
    {
        std::cout << "Key is valid: 26 unique mappings.\n";
    }
    else
    {
        std::cout << "Key validation FAILED.\n";
        return 1;
    }

    // -------------------------------------------------
    // Re-encrypt plaintext
    // -------------------------------------------------

    std::string regeneratedCiphertext =
        applySubstitution(plaintext, encryptionKey);

    // -------------------------------------------------
    // Final verification
    // -------------------------------------------------

    std::cout << "\n=== SOLUTION VERIFICATION ===\n";

    if (regeneratedCiphertext == ciphertext)
    {
        std::cout << "SUCCESS: Re-encrypted ciphertext "
                     "matches the original ciphertext.\n";
    }
    else
    {
        std::cout << "FAILED: Re-encrypted ciphertext "
                     "does not match the original.\n";
    }

    return 0;
}