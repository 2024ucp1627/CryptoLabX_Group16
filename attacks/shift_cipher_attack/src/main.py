from pathlib import Path

from shift_cipher import encrypt
from brute_force_dictionary import (
    brute_force,
    load_dictionary,
    find_best_key
)
from chi_square_attack import (
    get_all_scores,
    chi_square_attack
)


def main():

    print("=" * 60)
    print("SHIFT CIPHER CRYPTANALYSIS")
    print("=" * 60)

    # --------------------------------------------------
    # INPUT
    # --------------------------------------------------

    plaintext = input("\nEnter plaintext: ")

    actual_key = int(
        input("Enter encryption key (0-25): ")
    )

    if not 0 <= actual_key <= 25:
        print("Error: Key must be between 0 and 25.")
        return

    # --------------------------------------------------
    # ENCRYPTION
    # --------------------------------------------------

    plaintext = plaintext.upper()

    ciphertext = encrypt(
        plaintext,
        actual_key
    )

    print("\nCiphertext:")
    print(ciphertext)

    # --------------------------------------------------
    # BRUTE FORCE ATTACK
    # --------------------------------------------------

    print("\n" + "=" * 60)
    print("BRUTE FORCE ATTACK")
    print("=" * 60)

    brute_force_results = brute_force(
        ciphertext
    )

    for key, candidate in brute_force_results:
        print(f"Key {key:2d} → {candidate}")

    # --------------------------------------------------
    # DICTIONARY ATTACK
    # --------------------------------------------------

    print("\n" + "=" * 60)
    print("DICTIONARY ATTACK")
    print("=" * 60)

    src_directory = Path(__file__).resolve().parent

    dictionary_path = (
        src_directory.parent
        / "dictionary"
        / "english_words.txt"
    )

    dictionary = load_dictionary(
        dictionary_path
    )

    dictionary_key, dictionary_plaintext, dictionary_score_value = (
        find_best_key(
            ciphertext,
            dictionary
        )
    )

    print("Predicted Key    :", dictionary_key)
    print("Plaintext        :", dictionary_plaintext)
    print("Dictionary Score :", dictionary_score_value)

    # --------------------------------------------------
    # CHI-SQUARE ATTACK
    # --------------------------------------------------

    print("\n" + "=" * 60)
    print("CHI-SQUARE ATTACK")
    print("=" * 60)

    chi_results = get_all_scores(
        ciphertext
    )

    print("\nChi-Square Scores:")
    print("-" * 40)

    for key, score, candidate in chi_results:
        print(f"Key {key:2d} → {score:.2f}")

    chi_key, chi_plaintext, chi_score = (
        chi_square_attack(
            ciphertext
        )
    )

    print("\nPredicted Key     :", chi_key)
    print("Plaintext         :", chi_plaintext)
    print("Chi-Square Score  :", chi_score)

    # --------------------------------------------------
    # FINAL COMPARISON
    # --------------------------------------------------

    dictionary_correct = (
        dictionary_key == actual_key
    )

    chi_square_correct = (
        chi_key == actual_key
    )

    print("\n" + "=" * 60)
    print("FINAL COMPARISON")
    print("=" * 60)

    print("\nActual Key          :", actual_key)
    print("Dictionary Key      :", dictionary_key)
    print("Chi-Square Key      :", chi_key)

    print(
        "Dictionary Correct? :",
        "YES" if dictionary_correct else "NO"
    )

    print(
        "Chi-Square Correct? :",
        "YES" if chi_square_correct else "NO"
    )

    print("\n" + "=" * 60)

    # --------------------------------------------------
    # SAVE RESULTS
    # --------------------------------------------------

    output_directory = (
        src_directory.parent
        / "outputs"
    )

    output_directory.mkdir(
        exist_ok=True
    )

    output_file = (
        output_directory
        / "results.txt"
    )

    with open(output_file, "a") as file:

        file.write("=" * 60 + "\n")
        file.write("SHIFT CIPHER CRYPTANALYSIS TEST\n")
        file.write("=" * 60 + "\n")

        file.write(
            f"Plaintext: {plaintext}\n"
        )

        file.write(
            f"Ciphertext: {ciphertext}\n"
        )

        file.write(
            f"Actual Key: {actual_key}\n"
        )

        file.write(
            f"Dictionary Key: {dictionary_key}\n"
        )

        file.write(
            f"Dictionary Score: {dictionary_score_value}\n"
        )

        file.write(
            f"Chi-Square Key: {chi_key}\n"
        )

        file.write(
            f"Chi-Square Score: {chi_score}\n"
        )

        file.write(
            f"Dictionary Correct: "
            f"{'YES' if dictionary_correct else 'NO'}\n"
        )

        file.write(
            f"Chi-Square Correct: "
            f"{'YES' if chi_square_correct else 'NO'}\n"
        )

        file.write("\n")

    print(
        f"\nResults saved to: {output_file}"
    )


if __name__ == "__main__":
    main()