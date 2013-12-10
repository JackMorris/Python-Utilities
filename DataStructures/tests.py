import binary_tree
import linked_list
import dequeue
import stack
import unittest
import random


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.b = binary_tree.BinaryTree()

    def test_empty_tree_contains_false(self):
        self.assertFalse(self.b.contains(random.randint(-1000000, 1000000)))

    def test_single_item_contains(self):
        value = random.randint(-1000000, 1000000)
        self.b.add(value)
        self.assertTrue(self.b.contains(value))

    def test_single_item_contains_false(self):
        value = random.randint(-100, 100)
        self.b.add(value)
        for i in range(-100, 101):
            self.assertFalse(self.b.contains(i) and i != value)

    def test_single_item_delete(self):
        self.b.add(10)
        self.b.delete(10)
        self.assertFalse(self.b.contains(10))

    def test_multiple_item_contains(self):
        for i in range(-100, 100):
            self.b.add(i)
        for i in range(-100, 100):
            self.assertTrue(self.b.contains(i))

    def test_multiple_item_contains_false(self):
        for i in range(-100, 100):
            self.b.add(i)
        for i in range(-500, -100):
            self.assertFalse(self.b.contains(i))
        for i in range(100, 500):
            self.assertFalse(self.b.contains(i))

    def test_multiple_item_delete(self):
        for i in range(-100, 100):
            self.b.add(i)
        values_to_remove = sorted(list({random.randint(-100, 100) for i in range(0, 50)}))
        for v in values_to_remove:
            self.b.delete(v)
        for i in range(-100, 100):
            if i in values_to_remove:
                self.assertFalse(self.b.contains(i))
            else:
                self.assertTrue(self.b.contains(i))


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.l = linked_list.LinkedList()

    def test_empty_list(self):
        self.assertTrue(self.l.is_empty())

    def test_single_item_append_non_empty(self):
        self.l.append(random.randint(-1000000, 1000000))
        self.assertFalse(self.l.is_empty())

    def test_single_item_add_non_empty(self):
        self.l.add(random.randint(-1000000, 1000000), 0)
        self.assertFalse(self.l.is_empty())

    def test_single_item_append_value(self):
        value = random.randint(-1000000, 1000000)
        self.l.append(value)
        ret_value = self.l.get(0)
        self.assertEqual(value, ret_value)

    def test_single_item_add_value(self):
        value = random.randint(-1000000, 1000000)
        self.l.add(value, 0)
        ret_value = self.l.get(0)
        self.assertEqual(value, ret_value)

    def test_single_item_remove_empty(self):
        self.l.append(random.randint(-1000000, 1000000))
        self.l.remove(0)
        self.assertTrue(self.l.is_empty())

    def test_multi_item_contains(self):
        for i in range(0, 100):
            self.l.append(i)
        for i in range(0, 100):
            self.assertTrue(self.l.contains(i))

    def test_multi_item_contains_false(self):
        for i in range(0, 100):
            self.l.append(i)
        for i in range(-10, 0):
            self.assertFalse(self.l.contains(i))
        for i in range(100, 110):
            self.assertFalse(self.l.contains(i))

    def test_multi_item_get(self):
        for i in range(0, 1000):
            self.l.append(i**2)
        for i in range(0, 10):
            index = random.randint(0, 999)
            val = self.l.get(index)
            self.assertEqual(val, index**2)

    def test_multi_item_set(self):
        for i in range(0, 1000):
            self.l.append(1)
        for i in range(0, 1000):
            self.l.set(i*2, i)
        for i in range(0, 10):
            index = random.randint(0, 999)
            val = self.l.get(index)
            self.assertEqual(val, index*2)

    def test_multi_item_remove(self):
        for i in range(0, 1000):
            self.l.append(i)
        indices_to_remove = sorted(list({random.randint(0, 900) for i in range(0, 10)}))
        for i in indices_to_remove:
            self.l.remove(i)
        number_of_values = 1000 - len(indices_to_remove)
        for i in range(0, 100):
            index = random.randint(0, number_of_values-1)
            value = self.l.get(index)
            expected = index + len([j for j in indices_to_remove if j <= index])
            self.assertEqual(value, expected)


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = dequeue.MyQueue()

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
        self.s = stack.Stack()

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