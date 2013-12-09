from queue import *
from stack import *
import unittest
import random


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_empty_queue(self):
        self.assertTrue(self.q.is_empty())

    def test_single_item_non_empty(self):
        self.q.enqueue(random.randint(-1000000, 1000000))
        self.assertFalse(self.q.is_empty())

    def test_single_item_enqueue_dequeue_empty(self):
        self.q.enqueue(random.randint(-1000000, 1000000))
        self.q.dequeue()
        self.assertTrue(self.q.is_empty())

    def test_single_item_enqueue_dequeue_value(self):
        value = random.randint(-1000000, 1000000)
        self.q.enqueue(value)
        pop_value = self.q.dequeue()
        self.assertEqual(value, pop_value)

    def test_multi_item_enqueue_dequeue_non_empty(self):
        for i in range(0, random.randint(10,100)):
            self.q.enqueue(random.randint(-1000000, 1000000))
        self.assertFalse(self.q.is_empty())

    def test_multi_item_enqueue_dequeue_empty(self):
        for i in range(0, 1000):
            self.q.enqueue(random.randint(-1000000, 1000000))
        for i in range(0, 1000):
            self.q.dequeue()
        self.assertTrue(self.q.is_empty())

    def test_multi_item_enqueue_dequeue_value(self):
        for i in range(-100, 100):
            self.q.enqueue(i)
        for i in range(-100, 100):
            self.assertEqual(self.q.dequeue(), i)


class TestStack(unittest.TestCase):
    def setUp(self):
        self.s = Stack()

    def test_empty_stack(self):
        self.assertTrue(self.s.is_empty())

    def test_single_item_non_empty(self):
        self.s.push(random.randint(-1000000, 1000000))
        self.assertFalse(self.s.is_empty())

    def test_single_item_push_pop_empty(self):
        self.s.push(random.randint(-1000000, 1000000))
        self.s.pop()
        self.assertTrue(self.s.is_empty())

    def test_single_item_push_pop_value(self):
        value = random.randint(-1000000, 1000000)
        self.s.push(value)
        pop_value = self.s.pop()
        self.assertEqual(value, pop_value)

    def test_multi_item_push_pop_non_empty(self):
        for i in range(0, random.randint(10,100)):
            self.s.push(random.randint(-1000000, 1000000))
        self.assertFalse(self.s.is_empty())

    def test_multi_item_push_pop_empty(self):
        for i in range(0, 1000):
            self.s.push(random.randint(-1000000, 1000000))
        for i in range(0, 1000):
            self.s.pop()
        self.assertTrue(self.s.is_empty())

    def test_multi_item_push_pop_value(self):
        for i in range(-100, 100):
            self.s.push(i)
        for i in range(99, -101, -1):
            self.assertEqual(self.s.pop(), i)


if __name__ == 'main':
    unittest.main()