from shift_cipher import decrypt


ENGLISH_FREQUENCIES = {
    'A': 8.167,
    'B': 1.492,
    'C': 2.782,
    'D': 4.253,
    'E': 12.702,
    'F': 2.228,
    'G': 2.015,
    'H': 6.094,
    'I': 6.966,
    'J': 0.153,
    'K': 0.772,
    'L': 4.025,
    'M': 2.406,
    'N': 6.749,
    'O': 7.507,
    'P': 1.929,
    'Q': 0.095,
    'R': 5.987,
    'S': 6.327,
    'T': 9.056,
    'U': 2.758,
    'V': 0.978,
    'W': 2.360,
    'X': 0.150,
    'Y': 1.974,
    'Z': 0.074
}


def calculate_chi_square(text):

    # Keep only alphabetic characters
    letters = [
        char.upper()
        for char in text
        if char.isalpha()
    ]

    # Frequency analysis is impossible without letters
    if not letters:
        return float("inf")

    total_letters = len(letters)

    # Count occurrences of each letter
    observed_counts = {
        char: 0
        for char in ENGLISH_FREQUENCIES
    }

    for char in letters:
        observed_counts[char] += 1

    chi_square = 0.0

    # Calculate Chi-Square statistic
    for char in ENGLISH_FREQUENCIES:

        observed = observed_counts[char]

        expected = (
            ENGLISH_FREQUENCIES[char] / 100
        ) * total_letters

        chi_square += (
            (observed - expected) ** 2
        ) / expected

    return chi_square


def get_all_scores(ciphertext):

    results = []

    for key in range(26):

        plaintext = decrypt(
            ciphertext,
            key
        )

        score = calculate_chi_square(
            plaintext
        )

        results.append(
            (key, score, plaintext)
        )

    return results


def chi_square_attack(ciphertext):


    results = get_all_scores(ciphertext)

    best_key, best_score, best_plaintext = min(
        results,
        key=lambda x: x[1]
    )

    return best_key, best_plaintext, best_score