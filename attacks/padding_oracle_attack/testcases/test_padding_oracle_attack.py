import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from padding_oracle_attack import encrypt_message, PaddingOracle, padding_oracle_attack


class PaddingOracleAttackTests(unittest.TestCase):
    def test_recover_various_plaintexts(self):
        messages = [
            b"hello",
            b"A" * 16,
            b"Different length test message.",
            os.urandom(32),
        ]

        for message in messages:
            with self.subTest(length=len(message)):
                key, iv, ciphertext = encrypt_message(message)
                oracle = PaddingOracle(key)
                recovered = padding_oracle_attack(iv, ciphertext, oracle)
                self.assertEqual(recovered, message)
                self.assertGreater(oracle.queries, 0)


if __name__ == "__main__":
    unittest.main()
