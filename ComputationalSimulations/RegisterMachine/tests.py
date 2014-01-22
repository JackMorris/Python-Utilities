import unittest
import random
from encoder import Encoder
from decoder import Decoder


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

    def test_encode_program_instructions_empty(self):
        self.assertEqual(Encoder.encode_program_instructions([]), 0)

    def test_encode_program_instructions_two(self):
        self.assertEqual(Encoder.encode_program_instructions(["R0- -> L0, L2", "HALT"]), 786432)

    def test_encode_program_instructions_five(self):
        program_instructions = ["R0+ -> L0", "R0+ -> L0", "HALT", "R0- -> L0, L0", "R0+ -> L0"]
        self.assertEqual(Encoder.encode_program_instructions(program_instructions), 666)

    def test_encode_program_instructions_incorrect_format_raise(self):
        self.assertRaises(ValueError, Encoder.encode_program_instructions, ["Ro+ -> L1", "-> L2"])


class TestDecoder(unittest.TestCase):
    def test_decode_pair_zero(self):
        self.assertEqual(Decoder.decode_pair(0, fat=False), (0, 0))

    def test_decode_pair_one_fat(self):
        self.assertEqual(Decoder.decode_pair(1), (0, 0))

    def test_decode_pair_fat(self):
        self.assertEqual(Decoder.decode_pair(396), (2, 49))

    def test_decode_pair(self):
        self.assertEqual(Decoder.decode_pair(415, fat=False), (5, 6))

    def test_decode_list_negative_raises(self):
        self.assertRaises(ValueError, Decoder.decode_list, [2, 3, -4, 1])

    def test_decode_list_non_int_raises(self):
        self.assertRaises(ValueError, Decoder.decode_list, [1, 7, 'Hello, world!', 4])

    def test_decode_list_empty(self):
        self.assertEqual(Decoder.decode_list(0), [])

    def test_decode_list_single_value(self):
        self.assertEqual(Decoder.decode_list(8), [3])

    def test_decode_list_three_values(self):
        self.assertEqual(Decoder.decode_list(276), [2, 1, 3])

    def test_decode_program_instructions_empty(self):
        self.assertEqual(Decoder.decode_program_instructions(0), [])

    def test_decode_program_instructions_two(self):
        self.assertEqual(Decoder.decode_program_instructions(786432), ["R0- -> L0, L2", "HALT"])

    def test_decode_program_instructions_five(self):
        program_instructions = ["R0+ -> L0", "R0+ -> L0", "HALT", "R0- -> L0, L0", "R0+ -> L0"]
        self.assertEqual(Decoder.decode_program_instructions(666), program_instructions)

    def test_decode_program_negative_raises(self):
        self.assertRaises(ValueError, Decoder.decode_program_instructions, -3)

    def test_decode_program_non_int_raises(self):
        self.assertRaises(ValueError, Decoder.decode_program_instructions, 'Hello, world!')


class TestEncodeDecode(unittest.TestCase):
    def test_encode_decode_pair(self):
        x = random.randint(0, 10000)
        y = random.randint(0, 10000)
        self.assertEqual(Decoder.decode_pair(Encoder.encode_pair((x, y))), (x, y))

    def test_decode_encode_pair(self):
        numerical_representation = random.randint(1, 10000)
        self.assertEqual(Encoder.encode_pair(Decoder.decode_pair(numerical_representation)), numerical_representation)

    def test_encode_decode_list(self):
        check_list = []
        for i in range(0, random.randint(5, 15)):
            check_list.append(random.randint(0, 500))
        self.assertEqual(Decoder.decode_list(Encoder.encode_list(check_list)), check_list)

    def test_decode_encode_list(self):
        numerical_representation = random.randint(1, 10000)
        self.assertEqual(Encoder.encode_list(Decoder.decode_list(numerical_representation)), numerical_representation)

    def test_decode_encode_program(self):
        numerical_representation = random.randint(100, 10000)
        self.assertEqual(Encoder.encode_program_instructions(
            Decoder.decode_program_instructions(numerical_representation)), numerical_representation)