import unittest
import shift_cipher


class TestShiftCipher(unittest.TestCase):
    def test_single_character_encode(self):
       self.assertEqual(shift_cipher.encode("C", "N"), "P")

    def test_string_encode(self):
        self.assertEqual(shift_cipher.encode("HELLO WORLD", "C"), "JGNNQ YQTNF")