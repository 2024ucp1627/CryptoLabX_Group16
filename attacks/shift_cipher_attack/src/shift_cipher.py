def encrypt(text, key):
    result = ""

    for char in text:
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            result += char

    return result


def decrypt(text, key):
    return encrypt(text, -key)


# Test
plaintext = "HELLO WORLD"
key = 3

ciphertext = encrypt(plaintext, key)

print("Plaintext :", plaintext)
print("Key       :", key)
print("Ciphertext:", ciphertext)
print("Decrypted :", decrypt(ciphertext, key))
