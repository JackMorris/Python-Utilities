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
    while count > 0:
        result_list.append(random.randint(min_val, max_val))
        count -= 1
    return result_list


class BubbleSort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        bubble_sort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = [random.randint(-1000000, 1000000)]
        data_cp = data[:]
        bubble_sort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = [random.randint(-1000000, 1000000), random.randint(-1000000, 1000000)]
        data_correct = data[:]
        if data_correct[0] > data_correct[1]:
            tmp = data_correct[0]
            data_correct[0] = data_correct[1]
            data_correct[1] = tmp
        bubble_sort(data)
        self.assertEqual(data, data_correct)

    def test_array_input(self):
        data = rand_list()
        bubble_sort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])


class CountingSort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        counting_sort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = [random.randint(-1000000, 1000000)]
        data_cp = data[:]
        counting_sort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = [random.randint(-1000000, 1000000), random.randint(-1000000, 1000000)]
        data_correct = data[:]
        if data_correct[0] > data_correct[1]:
            tmp = data_correct[0]
            data_correct[0] = data_correct[1]
            data_correct[1] = tmp
        counting_sort(data)
        self.assertEqual(data, data_correct)

    def test_array_input(self):
        data = rand_list()
        counting_sort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])


class HeapSort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        heap_sort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = [random.randint(-1000000, 1000000)]
        data_cp = data[:]
        heap_sort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = [random.randint(-1000000, 1000000), random.randint(-1000000, 1000000)]
        data_correct = data[:]
        if data_correct[0] > data_correct[1]:
            tmp = data_correct[0]
            data_correct[0] = data_correct[1]
            data_correct[1] = tmp
        heap_sort(data)
        self.assertEqual(data, data_correct)

    def test_array_input(self):
        data = rand_list()
        heap_sort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])


class InsertionSort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        insertion_sort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = [random.randint(-1000000, 1000000)]
        data_cp = data[:]
        insertion_sort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = [random.randint(-1000000, 1000000), random.randint(-1000000, 1000000)]
        data_correct = data[:]
        if data_correct[0] > data_correct[1]:
            tmp = data_correct[0]
            data_correct[0] = data_correct[1]
            data_correct[1] = tmp
        insertion_sort(data)
        self.assertEqual(data, data_correct)

    def test_array_input(self):
        data = rand_list()
        insertion_sort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])


class MergeSort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        merge_sort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = [random.randint(-1000000, 1000000)]
        data_cp = data[:]
        merge_sort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = [random.randint(-1000000, 1000000), random.randint(-1000000, 1000000)]
        data_correct = data[:]
        if data_correct[0] > data_correct[1]:
            tmp = data_correct[0]
            data_correct[0] = data_correct[1]
            data_correct[1] = tmp
        merge_sort(data)
        self.assertEqual(data, data_correct)

    def test_array_input(self):
        data = rand_list()
        merge_sort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])


class Quicksort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        quicksort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = [random.randint(-1000000, 1000000)]
        data_cp = data[:]
        quicksort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = [random.randint(-1000000, 1000000), random.randint(-1000000, 1000000)]
        data_correct = data[:]
        if data_correct[0] > data_correct[1]:
            tmp = data_correct[0]
            data_correct[0] = data_correct[1]
            data_correct[1] = tmp
        quicksort(data)
        self.assertEqual(data, data_correct)

    def test_array_input(self):
        data = rand_list()
        quicksort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])


class RadixSort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        radix_sort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = [random.randint(0, 1000000)]
        data_cp = data[:]
        radix_sort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = [random.randint(0, 1000000), random.randint(0, 1000000)]
        data_correct = data[:]
        if data_correct[0] > data_correct[1]:
            tmp = data_correct[0]
            data_correct[0] = data_correct[1]
            data_correct[1] = tmp
        radix_sort(data)
        self.assertEqual(data, data_correct)

    def test_array_input(self):
        data = rand_list(min_val=0)
        radix_sort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])


class SelectionSort(unittest.TestCase):
    def test_zero_input(self):
        data = []
        selection_sort(data)
        self.assertEqual(data, [])

    def test_single_input(self):
        data = [random.randint(-1000000, 1000000)]
        data_cp = data[:]
        selection_sort(data)
        self.assertEqual(data, data_cp)

    def test_double_input(self):
        data = [random.randint(-1000000, 1000000), random.randint(-1000000, 1000000)]
        data_correct = data[:]
        if data_correct[0] > data_correct[1]:
            tmp = data_correct[0]
            data_correct[0] = data_correct[1]
            data_correct[1] = tmp
        selection_sort(data)
        self.assertEqual(data, data_correct)

    def test_array_input(self):
        data = rand_list()
        selection_sort(data)
        for i in range(1, len(data)):
            self.assertLessEqual(data[i-1], data[i])

if __name__ == 'main':
    unittest.main()