from bubble_sort import *
from counting_sort import *
from heap_sort import *
from insertion_sort import *
from merge_sort import *
from quicksort import *
from radix_sort import *
from selection_sort import *
import unittest
import random


def rand_list(count=100, min_val=-1000000, max_val=1000000):
    result_list = []
    for i in range(count, 0, -1):
        result_list.append(random.randint(min_val, max_val))
    return result_list


class TestBubbleSort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        bubble_sort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = rand_list(count=1)
        data_cp = data[:]
        bubble_sort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = rand_list(count=2)
        bubble_sort(data)
        self.assertLessEqual(data[0], data[1])

    def test_array_input(self):
        data = rand_list()
        bubble_sort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])

    def test_all_zero_input(self):
        data = [0]*100
        bubble_sort(data)
        for i in range(0, 100):
            self.assertEqual(data[i], 0)

    def test_all_same_input(self):
        single_val = rand_list(count=1)[0]
        data = [single_val]*100
        bubble_sort(data)
        for i in range(0, 100):
            self.assertEqual(single_val, data[i])


class TestCountingSort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        counting_sort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = rand_list(count=1)
        data_cp = data[:]
        counting_sort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = rand_list(count=2)
        counting_sort(data)
        self.assertLessEqual(data[0], data[1])

    def test_array_input(self):
        data = rand_list()
        counting_sort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])

    def test_all_zero_input(self):
        data = [0]*100
        counting_sort(data)
        for i in range(0, 100):
            self.assertEqual(data[i], 0)

    def test_all_same_input(self):
        single_val = rand_list(count=1)[0]
        data = [single_val]*100
        counting_sort(data)
        for i in range(0, 100):
            self.assertEqual(single_val, data[i])


class TestHeapSort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        heap_sort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = rand_list(count=1)
        data_cp = data[:]
        heap_sort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = rand_list(count=2)
        heap_sort(data)
        self.assertLessEqual(data[0], data[1])

    def test_array_input(self):
        data = rand_list()
        heap_sort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])

    def test_all_zero_input(self):
        data = [0]*100
        heap_sort(data)
        for i in range(0, 100):
            self.assertEqual(data[i], 0)

    def test_all_same_input(self):
        single_val = rand_list(count=1)[0]
        data = [single_val]*100
        heap_sort(data)
        for i in range(0, 100):
            self.assertEqual(single_val, data[i])


class TestInsertionSort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        insertion_sort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = rand_list(count=1)
        data_cp = data[:]
        insertion_sort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = rand_list(count=2)
        insertion_sort(data)
        self.assertLessEqual(data[0], data[1])

    def test_array_input(self):
        data = rand_list()
        insertion_sort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])

    def test_all_zero_input(self):
        data = [0]*100
        insertion_sort(data)
        for i in range(0, 100):
            self.assertEqual(data[i], 0)

    def test_all_same_input(self):
        single_val = rand_list(count=1)[0]
        data = [single_val]*100
        insertion_sort(data)
        for i in range(0, 100):
            self.assertEqual(single_val, data[i])


class TestMergeSort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        merge_sort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = rand_list(count=1)
        data_cp = data[:]
        merge_sort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = rand_list(count=2)
        merge_sort(data)
        self.assertLessEqual(data[0], data[1])

    def test_array_input(self):
        data = rand_list()
        merge_sort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])

    def test_all_zero_input(self):
        data = [0]*100
        merge_sort(data)
        for i in range(0, 100):
            self.assertEqual(data[i], 0)

    def test_all_same_input(self):
        single_val = rand_list(count=1)[0]
        data = [single_val]*100
        merge_sort(data)
        for i in range(0, 100):
            self.assertEqual(single_val, data[i])


class TestQuicksort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        quicksort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = rand_list(count=1)
        data_cp = data[:]
        quicksort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = rand_list(count=2)
        quicksort(data)
        self.assertLessEqual(data[0], data[1])

    def test_array_input(self):
        data = rand_list()
        quicksort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])

    def test_all_zero_input(self):
        data = [0]*100
        quicksort(data)
        for i in range(0, 100):
            self.assertEqual(data[i], 0)

    def test_all_same_input(self):
        single_val = rand_list(count=1)[0]
        data = [single_val]*100
        quicksort(data)
        for i in range(0, 100):
            self.assertEqual(single_val, data[i])


class TestRadixSort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        radix_sort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = rand_list(min_val=0, count=1)
        data_cp = data[:]
        radix_sort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = rand_list(min_val=0, count=2)
        radix_sort(data)
        self.assertLessEqual(data[0], data[1])

    def test_array_input(self):
        data = rand_list(min_val=0)
        radix_sort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])

    def test_all_zero_input(self):
        data = [0]*100
        radix_sort(data)
        for i in range(0, 100):
            self.assertEqual(data[i], 0)

    def test_all_same_input(self):
        single_val = rand_list(count=1, min_val=0)[0]
        data = [single_val]*100
        radix_sort(data)
        for i in range(0, 100):
            self.assertEqual(single_val, data[i])


class TestSelectionSort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        selection_sort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = rand_list(count=1)
        data_cp = data[:]
        selection_sort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = rand_list(count=2)
        selection_sort(data)
        self.assertLessEqual(data[0], data[1])

    def test_array_input(self):
        data = rand_list()
        selection_sort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])

    def test_all_zero_input(self):
        data = [0]*100
        selection_sort(data)
        for i in range(0, 100):
            self.assertEqual(data[i], 0)

    def test_all_same_input(self):
        single_val = rand_list(count=1)[0]
        data = [single_val]*100
        selection_sort(data)
        for i in range(0, 100):
            self.assertEqual(single_val, data[i])

if __name__ == 'main':
    unittest.main()