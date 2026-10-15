from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


BLOCK_SIZE = AES.block_size


class PaddingOracle:
    """Demonstration oracle: reports only whether PKCS#7 padding is valid."""

    def __init__(self, key):
        self.__key = key
        self.queries = 0

    def check(self, iv, ciphertext):
        self.queries += 1
        try:
            cipher = AES.new(self.__key, AES.MODE_CBC, iv=iv)
            plaintext = cipher.decrypt(ciphertext)
            unpad(plaintext, BLOCK_SIZE, style="pkcs7")
            return True
        except ValueError:
            return False


def encrypt_message(plaintext):
    """Demo setup only. The attack never receives the key."""
    key = get_random_bytes(BLOCK_SIZE)
    iv = get_random_bytes(BLOCK_SIZE)
    ciphertext = AES.new(key, AES.MODE_CBC, iv=iv).encrypt(
        pad(plaintext, BLOCK_SIZE, style="pkcs7")
    )
    return key, iv, ciphertext


def recover_intermediate_block(target_block, oracle):
    """
    Recover AES-decrypt(target_block), one byte at a time.
    Only the oracle is used; the AES key is never accessed.
    """
    intermediate = bytearray(BLOCK_SIZE)
    crafted_iv = bytearray(BLOCK_SIZE)

    for padding_value in range(1, BLOCK_SIZE + 1):
        index = BLOCK_SIZE - padding_value

        # Force already-recovered suffix bytes to the desired padding.
        for j in range(index + 1, BLOCK_SIZE):
            crafted_iv[j] = intermediate[j] ^ padding_value

        found = False

        for guess in range(256):
            crafted_iv[index] = guess

            if not oracle.check(bytes(crafted_iv), target_block):
                continue

            # Reject false positives caused by a longer pre-existing padding.
            if index > 0:
                confirmation = bytearray(crafted_iv)
                confirmation[index - 1] ^= 1
                if not oracle.check(bytes(confirmation), target_block):
                    continue

            intermediate[index] = guess ^ padding_value
            found = True
            break

        if not found:
            raise RuntimeError(
                f"Could not recover byte at block offset {index}"
            )

    return bytes(intermediate)


def padding_oracle_attack(iv, ciphertext, oracle):
    """Recover and unpad plaintext without access to the AES key."""
    if len(iv) != BLOCK_SIZE:
        raise ValueError("IV must be exactly one AES block (16 bytes).")
    if not ciphertext or len(ciphertext) % BLOCK_SIZE != 0:
        raise ValueError("Ciphertext must contain complete AES blocks.")

    recovered = bytearray()
    previous = iv

    for offset in range(0, len(ciphertext), BLOCK_SIZE):
        target = ciphertext[offset:offset + BLOCK_SIZE]
        intermediate = recover_intermediate_block(target, oracle)

        plaintext_block = bytes(
            intermediate[i] ^ previous[i] for i in range(BLOCK_SIZE)
        )
        recovered.extend(plaintext_block)
        previous = target

    return unpad(bytes(recovered), BLOCK_SIZE, style="pkcs7")


def main():
    # Demo fixture: replace this setup with the instructor's supplied
    # IV and ciphertext if they provided them separately.
    original = (
        b"Padding oracle attacks exploit distinguishable padding errors. "
        b"Use authenticated encryption to prevent this vulnerability."
    )

    key, iv, ciphertext = encrypt_message(original)
    oracle = PaddingOracle(key)

    print("IV:", iv.hex())
    print("Ciphertext:", ciphertext.hex())

    # From this point on, the attack receives no key.
    recovered = padding_oracle_attack(iv, ciphertext, oracle)

    print("\nRecovered plaintext:", recovered.decode("utf-8"))
    print("Oracle queries:", oracle.queries)
    print("Demo verification:", recovered == original)


if __name__ == "__main__":
    main()
