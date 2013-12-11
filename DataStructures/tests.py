import binary_search_tree
import binary_tree
import linked_list
import dequeue
import stack
import unittest
import random
import veb_tree


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = binary_search_tree.BinarySearchTree()

    def test_empty_tree_contains_false(self):
        self.assertFalse(self.bst.contains(random.randint(-1000000, 1000000)))

    def test_single_item_contains(self):
        key = random.randint(-1000000, 1000000)
        self.bst.set(key, 0)
        self.assertTrue(self.bst.contains(key))

    def test_single_item_contains_false(self):
        key = random.randint(-100, 100)
        self.bst.set(key, 0)
        for i in range(-100, 101):
            self.assertFalse(self.bst.contains(i) and i != key)

    def test_single_item_get(self):
        key = random.randint(-100, 100)
        value = random.randint(-100, 100)
        self.bst.set(key, value)
        self.assertEqual(value, self.bst.get(key))

    def test_multiple_item_get(self):
        for i in range(-100, 100):
            self.bst.set(i, i*2)
        for i in range(-100, 100):
            self.assertEqual(i*2, self.bst.get(i))

    def test_single_item_set(self):
        key = random.randint(-100, 100)
        value = random.randint(100, 200)
        self.bst.set(key, 0)
        self.bst.set(key, value)
        self.assertEqual(self.bst.get(key), value)

    def test_multiple_item_set(self):
        for i in range(-100, 100):
            self.bst.set(i, -1)
        for i in range(-100, 100):
            self.bst.set(i, i**2)
        for i in range(-100, 100):
            self.assertEqual(self.bst.get(i), i**2)

    def test_single_item_delete(self):
        self.bst.set(10, 0)
        self.bst.delete(10)
        self.assertFalse(self.bst.contains(10))

    def test_multiple_item_contains(self):
        for i in range(-100, 100):
            self.bst.set(i, 0)
        for i in range(-100, 100):
            self.assertTrue(self.bst.contains(i))

    def test_multiple_item_contains_false(self):
        for i in range(-100, 100):
            self.bst.set(i, 0)
        for i in range(-500, -100):
            self.assertFalse(self.bst.contains(i))
        for i in range(100, 500):
            self.assertFalse(self.bst.contains(i))

    def test_multiple_item_delete(self):
        for i in range(-100, 100):
            self.bst.set(i, 0)
        values_to_delete = sorted(list({random.randint(-100, 99) for i in range(0, 50)}))
        for v in values_to_delete:
            self.bst.delete(v)
        for i in range(-100, 100):
            if i in values_to_delete:
                self.assertFalse(self.bst.contains(i))
            else:
                self.assertTrue(self.bst.contains(i))


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
        values_to_delete = sorted(list({random.randint(-100, 99) for i in range(0, 50)}))
        for v in values_to_delete:
            self.b.delete(v)
        for i in range(-100, 100):
            if i in values_to_delete:
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

    def test_single_item_delete_empty(self):
        self.l.append(random.randint(-1000000, 1000000))
        self.l.delete(0)
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

    def test_multi_item_delete(self):
        for i in range(0, 1000):
            self.l.append(i)
        indices_to_delete = sorted(list({random.randint(0, 900) for i in range(0, 10)}))
        for i in indices_to_delete:
            self.l.delete(i)
        number_of_values = 1000 - len(indices_to_delete)
        for i in range(0, 100):
            index = random.randint(0, number_of_values-1)
            value = self.l.get(index)
            expected = index + len([j for j in indices_to_delete if j <= index])
            self.assertEqual(value, expected)


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = dequeue.DeQueue()

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


class TestvEB(unittest.TestCase):
    def setUp(self):
        self.v = veb_tree.vEBTree(2)

    def test_single_item_minimum(self):
        value = random.randint(0, 15)
        self.v.insert(value)
        self.assertEqual(self.v.minimum(), value)

    def test_multiple_item_minimum(self):
        values = {random.randint(0, 15) for i in range(0, 6)}
        for v in values:
            self.v.insert(v)
        self.assertEqual(self.v.minimum(), min(values))

    def test_single_item_maximum(self):
        value = random.randint(0, 15)
        self.v.insert(value)
        self.assertEqual(self.v.maximum(), value)

    def test_multiple_item_maximum(self):
        values = {random.randint(0, 15) for i in range(0, 6)}
        for v in values:
            self.v.insert(v)
        self.assertEqual(self.v.maximum(), max(values))

    def test_single_item_member(self):
        value = random.randint(0, 15)
        self.v.insert(value)
        for i in range(0, 16):
            if i == value:
                self.assertTrue(self.v.member(i))
            else:
                self.assertFalse((self.v.member(i)))

    def test_multiple_item_member(self):
        values = {random.randint(0, 15) for i in range(0, 6)}
        for v in values:
            self.v.insert(v)
        for i in range(0, 16):
            if i in values:
                self.assertTrue(self.v.member(i))
            else:
                self.assertFalse(self.v.member(i))

    def test_all_item_member(self):
        for i in range(0, 16):
            self.v.insert(i)
        for i in range(0, 16):
            self.assertTrue(self.v.member(i))

    def test_successor(self):
        values = []
        while len(values) < 2:
            values = sorted(list({random.randint(0, 15) for i in range(0, 6)}))
        for v in values:
            self.v.insert(v)
        index = random.randint(0, len(values)-2)
        self.assertEqual(self.v.successor(values[index]), values[index + 1])

    def test_predecessor(self):
        values = []
        while len(values) < 2:
            values = sorted(list({random.randint(0, 15) for i in range(0, 6)}))
        for v in values:
            self.v.insert(v)
        index = random.randint(1, len(values)-1)
        self.assertEqual(self.v.predecessor(values[index]), values[index - 1])

    def test_single_item_delete(self):
        value = random.randint(0, 15)
        self.v.insert(value)
        self.v.delete(value)
        self.assertFalse(self.v.member(value))

    def test_multiple_item_delete(self):
        for i in range(0, 16):
            self.v.insert(i)
        values_to_delete = {random.randint(0, 15) for i in range(0, 6)}
        for v in values_to_delete:
            self.v.delete(v)
        for i in range(0, 16):
            if i in values_to_delete:
                self.assertFalse(self.v.member(i))
            else:
                self.assertTrue(self.v.member(i))


if __name__ == 'main':
    unittest.main()