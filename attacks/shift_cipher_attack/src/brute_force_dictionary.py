from shift_cipher import decrypt


def brute_force(ciphertext):
    results = []

    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        results.append((key, plaintext))

    return results


def load_dictionary(filename):
    words = set()

    with open(filename, "r") as file:
        for line in file:
            word = line.strip().upper()

            if word:
                words.add(word)

    return words


def dictionary_score(text, dictionary):
    words = text.upper().split()

    score = 0

    for word in words:
        clean_word = ''.join(
            char for char in word if char.isalpha()
        )

        if clean_word in dictionary:
            score += 1

    return score


def find_best_key(ciphertext, dictionary):
    best_key = 0
    best_score = -1
    best_plaintext = ""

    for key in range(26):
        plaintext = decrypt(ciphertext, key)
        score = dictionary_score(plaintext, dictionary)

        if score > best_score:
            best_score = score
            best_key = key
            best_plaintext = plaintext

    return best_key, best_plaintext, best_score


if __name__ == "__main__":

    ciphertext = "KHOOR ZRUOG"

    dictionary_file = "../dictionary/english_words.txt"

    dictionary = load_dictionary(dictionary_file)

    print("BRUTE FORCE RESULTS")
    print("--------------------")

    for key, plaintext in brute_force(ciphertext):
        print(f"Key {key:2}: {plaintext}")

    print("\nDICTIONARY ATTACK")
    print("-----------------")

    key, plaintext, score = find_best_key(
        ciphertext,
        dictionary
    )

    print("Predicted Key :", key)
    print("Plaintext     :", plaintext)
    print("Score         :", score)
