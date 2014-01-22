import unittest
from encoder import Encoder


class TestEncoder(unittest.TestCase):
    def test_encode_pair_zero_fat(self):
        self.assertEqual(Encoder.encode_pair((0, 0)), 1)

    def test_encode_pair_zero(self):
        self.assertEqual(Encoder.encode_pair((0, 0), fat=False), 0)

    def test_encode_pair_first_zero_fat(self):
        self.assertEqual(Encoder.encode_pair((0, 2)), 5)

    def test_encode_pair_first_zero(self):
        self.assertEqual(Encoder.encode_pair((0, 2), fat=False), 4)

    def test_encode_pair_second_zero_fat(self):
        self.assertEqual(Encoder.encode_pair((2, 0)), 4)

    def test_encode_pair_second_zero(self):
        self.assertEqual(Encoder.encode_pair((2, 0), fat=False), 3)

    def test_encode_pair_fat(self):
        self.assertEqual(Encoder.encode_pair((7, 3)), 896)

    def test_encode_pair(self):
        self.assertEqual(Encoder.encode_pair((4, 12), fat=False), 399)

    def test_encode_pair_negative_first_raises(self):
        self.assertRaises(ValueError, Encoder.encode_pair, ((-1, 3)))

    def test_encode_pair_negative_second_raises(self):
        self.assertRaises(ValueError, Encoder.encode_pair, ((4, -2)))

    def test_encode_pair_non_int_first_raises(self):
        self.assertRaises(ValueError, Encoder.encode_pair, (('Hello, world!', 2)))

    def test_encode_pair_non_int_second_raises(self):
        self.assertRaises(ValueError, Encoder.encode_pair, (1, 'Hello, world!'))

    def test_encode_list_empty(self):
        self.assertEqual(Encoder.encode_list([]), 0)

    def test_encode_list_single_value(self):
        self.assertEqual(Encoder.encode_list([4]), 16)

    def test_encode_list_three_values(self):
        self.assertEqual(Encoder.encode_list([2, 1, 3]), 276)

    def test_encode_list_ten_values(self):
        self.assertEqual(Encoder.encode_list([1, 3, 2, 1, 2, 1, 3, 2, 1, 2]), 155755810)

    def test_encode_list_three_values_zero(self):
        self.assertEqual(Encoder.encode_list([2,0,4]), 268)

    def test_encode_list_negative_raises(self):
        self.assertRaises(ValueError, Encoder.encode_list, ([1, 2, 5, -4, 2, 1]))

    def test_encode_list_non_int_raises(self):
        self.assertRaises(ValueError, Encoder.encode_list, ([1, 2, 8, 'Hello, world!', 2]))