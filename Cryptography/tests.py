import unittest
import random
import shift_cipher


class TestShiftCipher(unittest.TestCase):
    def test_single_character_encode(self):
        self.assertEqual(shift_cipher.encode("C", "N"), "P")

    def test_string_encode(self):
        self.assertEqual(shift_cipher.encode("HELLO WORLD", "C"), "JGNNQ YQTNF")

    def test_single_character_decode(self):
        self.assertEqual(shift_cipher.decode("M", "C"), "K")

    def test_string_decode(self):
        self.assertEqual(shift_cipher.decode("HELLO WORLD", "C"), "FCJJM UMPJB")

    def test_encode_decode(self):
        for i in range(0, 100):
            plaintext = ""
            for j in range(0, random.randint(20, 50)):
                plaintext += chr(random.randint(65, 90))
            key = chr(random.randint(65, 90))
            self.assertEqual(shift_cipher.decode(shift_cipher.encode(plaintext, key), key), plaintext)

    def test_invalid_key_Raise(self):
        self.assertRaises(ValueError, shift_cipher.encode, "A", "_")

    def test_brute_force(self):
        brute_force_result = shift_cipher.brute_force_search("HELLO WORLD")
        for i in range(0, 26):
            self.assertEqual(shift_cipher.encode(brute_force_result[i], chr(i + 65)), "HELLO WORLD")