# Padding Oracle Attack on AES-CBC

## Objective
Demonstrate plaintext recovery from AES-CBC ciphertext using a
PKCS#7 padding-validity oracle, without accessing the AES key in the
attack implementation.

## Files
- `src/padding_oracle_attack.py`: encryption fixture, oracle, attack,
  recovered plaintext, and query counter.
- `testcases/test_padding_oracle_attack.py`: tests multiple plaintext lengths.
- `outputs/`: reserved for execution results.

## How it works
AES-CBC decryption follows:

P[i] = D_K(C[i]) XOR C[i-1]

For the first block, the IV replaces C[i-1]. Changing the previous
ciphertext block therefore changes the corresponding decrypted
plaintext block predictably.

PKCS#7 padding appends N bytes, each with value N, where N is between
1 and 16 for AES. The oracle reveals whether this padding is valid.

The attack modifies the preceding block, tries candidate byte values,
and uses oracle responses to recover the intermediate block D_K(C[i]).
XOR with the original preceding block recovers the plaintext. Bytes are
recovered from right to left, and the final padding is removed.

## Run
Install the dependency:

    python3 -m pip install pycryptodome

Run the demonstration from the repository root:

    python3 attacks/padding_oracle_attack/src/padding_oracle_attack.py

Run tests:

    python3 -m unittest discover -s attacks/padding_oracle_attack/testcases -p 'test_*.py' -v

## Query count
The program reports the actual number of oracle queries for each run.
The count varies with the generated key, IV, ciphertext, and candidate
search order. Each recovered block requires up to 16 rounds of 256
candidate guesses, with extra queries for confirmation.

## Security recommendation
Use authenticated encryption such as AES-GCM or ChaCha20-Poly1305.
If CBC must be retained, authenticate ciphertext and its IV before
decryption, use encrypt-then-MAC, and do not expose distinguishable
padding errors. Return uniform external errors and avoid leaking
decryption details through timing or other side channels.

## Important note
The default program creates a local demonstration ciphertext. If the
instructor supplied a particular ciphertext, IV, or starter oracle,
integrate those values and the supplied oracle before submitting.
