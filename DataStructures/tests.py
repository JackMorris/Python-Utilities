import binary_search_tree
import binary_tree
import linked_list
import queue
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
            if i != key:
                self.assertFalse(self.bst.contains(i))

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

    def test_multiple_item_contains_shuffle(self):
        shuffled_range = list(range(-100, 100))
        random.shuffle(shuffled_range)
        for i in shuffled_range:
            self.bst.set(i, 0)
        for i in range(-100, 100):
            self.assertTrue(self.bst.contains(i))

    def test_multiple_item_contains_false_shuffle(self):
        shuffled_range = list(range(-100, 100))
        random.shuffle(shuffled_range)
        for i in shuffled_range:
            self.bst.set(i, 0)
        for i in range(-500, -100):
            self.assertFalse(self.bst.contains(i))
        for i in range(100, 500):
            self.assertFalse(self.bst.contains(i))

    def test_single_item_get(self):
        key = random.randint(-100, 100)
        value = random.randint(-100, 100)
        self.bst.set(key, value)
        self.assertEqual(value, self.bst.get(key))

    def test_multiple_item_get(self):
        for i in range(-100, 100):
            self.bst.set(i, i)
        for i in range(-100, 100):
            self.assertEqual(i, self.bst.get(i))

    def test_multiple_item_get_shuffle(self):
        shuffled_range = list(range(-100, 100))
        random.shuffle(shuffled_range)
        for i in shuffled_range:
            self.bst.set(i, i)
        for i in range(-100, 100):
            self.assertEqual(i, self.bst.get(i))

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

    def test_multiple_item_set_shuffle(self):
        shuffled_range = list(range(-100, 100))
        random.shuffle(shuffled_range)
        for i in shuffled_range:
            self.bst.set(i, -1)
        random.shuffle(shuffled_range)
        for i in shuffled_range:
            self.bst.set(i, i**2)
        for i in range(-100, 100):
            self.assertEqual(self.bst.get(i), i**2)

    def test_single_item_delete(self):
        self.bst.set(10, 0)
        self.bst.delete(10)
        self.assertFalse(self.bst.contains(10))

    def test_multiple_item_delete(self):
        for i in range(-100, 100):
            self.bst.set(i, 0)
        values_to_delete = {random.randint(-100, 99) for i in range(0, 50)}
        for v in values_to_delete:
            self.bst.delete(v)
        for i in range(-100, 100):
            if i in values_to_delete:
                self.assertFalse(self.bst.contains(i))
            else:
                self.assertTrue(self.bst.contains(i))

    def test_single_root_delete(self):
        shuffled_range = list(range(-100, 100))
        random.shuffle(shuffled_range)
        for i in shuffled_range:
            self.bst.set(i, 0)
        self.bst.delete(-100)
        self.assertFalse(self.bst.contains(-100))
        for i in range(-99, 100):
            self.assertTrue(self.bst.contains(i))

    def test_multiple_root_delete(self):
        shuffled_range = list(range(-100, 100))
        random.shuffle(shuffled_range)
        for i in shuffled_range:
            self.bst.set(i, 0)
        for i in range(-100, 100):
            self.bst.delete(i)
            self.assertFalse(self.bst.contains(i))
            for j in range(i+1, 100):
                self.assertTrue(self.bst.contains(j))

    def test_all_items_delete(self):
        for i in range(-100, 100):
            self.bst.set(i, 0)
        for i in range(-100, 100):
            self.bst.delete(i)
        for i in range(-100, 100):
            self.assertFalse(self.bst.contains(i))


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.bt = binary_tree.BinaryTree()

    def test_empty_tree_contains_false(self):
        self.assertFalse(self.bt.contains(random.randint(-1000000, 1000000)))

    def test_single_item_contains(self):
        val = random.randint(-1000000, 1000000)
        self.bt.add(val)
        self.assertTrue(self.bt.contains(val))

    def test_single_item_contains_false(self):
        val = random.randint(-100, 100)
        self.bt.add(val)
        for i in range(-100, 101):
            if i != val:
                self.assertFalse(self.bt.contains(i))

    def test_multiple_item_contains(self):
        for i in range(-100, 100):
            self.bt.add(i)
        for i in range(-100, 100):
            self.assertTrue(self.bt.contains(i))

    def test_multiple_item_contains_false(self):
        for i in range(-100, 100):
            self.bt.add(i)
        for i in range(-500, -100):
            self.assertFalse(self.bt.contains(i))
        for i in range(100, 500):
            self.assertFalse(self.bt.contains(i))

    def test_multiple_item_contains_shuffle(self):
        shuffled_range = list(range(-100, 100))
        random.shuffle(shuffled_range)
        for i in shuffled_range:
            self.bt.add(i)
        for i in range(-100, 100):
            self.assertTrue(self.bt.contains(i))

    def test_multiple_item_contains_false_shuffle(self):
        shuffled_range = list(range(-100, 100))
        random.shuffle(shuffled_range)
        for i in shuffled_range:
            self.bt.add(i)
        for i in range(-500, -100):
            self.assertFalse(self.bt.contains(i))
        for i in range(100, 500):
            self.assertFalse(self.bt.contains(i))

    def test_single_item_delete(self):
        self.bt.add(10)
        self.bt.delete(10)
        self.assertFalse(self.bt.contains(10))

    def test_multiple_item_delete(self):
        for i in range(-100, 100):
            self.bt.add(i)
        values_to_delete = {random.randint(-100, 99) for i in range(0, 50)}
        for v in values_to_delete:
            self.bt.delete(v)
        for i in range(-100, 100):
            if i in values_to_delete:
                self.assertFalse(self.bt.contains(i))
            else:
                self.assertTrue(self.bt.contains(i))

    def test_single_root_delete(self):
        shuffled_range = list(range(-100, 100))
        random.shuffle(shuffled_range)
        for i in shuffled_range:
            self.bt.add(i)
        self.bt.delete(-100)
        self.assertFalse(self.bt.contains(-100))
        for i in range(-99, 100):
            self.assertTrue(self.bt.contains(i))

    def test_multiple_root_delete(self):
        shuffled_range = list(range(-100, 100))
        random.shuffle(shuffled_range)
        for i in shuffled_range:
            self.bt.add(i)
        for i in range(-100, 100):
            self.bt.delete(i)
            self.assertFalse(self.bt.contains(i))
            for j in range(i+1, 100):
                self.assertTrue(self.bt.contains(j))

    def test_all_items_delete(self):
        for i in range(-100, 100):
            self.bt.add(i)
        for i in range(-100, 100):
            self.bt.delete(i)
        for i in range(-100, 100):
            self.assertFalse(self.bt.contains(i))


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

    def test_single_item_append(self):
        value = random.randint(-1000000, 1000000)
        self.l.append(value)
        ret_value = self.l.get(0)
        self.assertEqual(value, ret_value)

    def test_single_item_add(self):
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
            self.l.append(i)
        for i in range(0, 1000):
            self.assertEqual(self.l.get(i), i)

    def test_multi_item_set(self):
        for i in range(0, 1000):
            self.l.append(-1)
        for i in range(0, 1000):
            self.l.set(i, i)
        for i in range(0, 1000):
            self.assertEqual(self.l.get(i), i)

    def test_multi_item_delete(self):
        for i in range(0, 1000):
            self.l.append(i)
        indices_to_delete = sorted(list({random.randint(0, 999) for i in range(0, 50)}), reverse=True)
        for i in indices_to_delete:
            self.l.delete(i)
        for i in range(0, 1000):
            if i in indices_to_delete:
                self.assertFalse(self.l.contains(i))
            else:
                self.assertTrue(self.l.contains(i))


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.q = queue.Queue()

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

    def test_multi_item_non_empty(self):
        for i in range(0, 10):
            self.s.push(random.randint(-1000000, 1000000))
        self.assertFalse(self.s.is_empty())

    def test_single_item_push_pop_empty(self):
        self.s.push(random.randint(-1000000, 1000000))
        self.s.pop()
        self.assertTrue(self.s.is_empty())

    def test_multi_item_push_pop_empty(self):
        for i in range(0, 1000):
            self.s.push(random.randint(-1000000, 1000000))
        for i in range(0, 1000):
            self.s.pop()
        self.assertTrue(self.s.is_empty())

    def test_single_item_push_pop(self):
        value = random.randint(-1000000, 1000000)
        self.s.push(value)
        pop_value = self.s.pop()
        self.assertEqual(value, pop_value)

    def test_multi_item_push_pop(self):
        for i in range(-100, 100):
            self.s.push(i)
        for i in range(99, -101, -1):
            self.assertEqual(self.s.pop(), i)

    def test_multi_item_push_pop_all_same(self):
        value = random.randint(-100, 100)
        for i in range(0, 100):
            self.s.push(value)
        for i in range(0, 100):
            self.assertEqual(self.s.pop(), value)

    def test_multi_item_push_pop_all_zero(self):
        for i in range(0, 100):
            self.s.push(0)
        for i in range(0, 100):
            self.assertEqual(self.s.pop(), 0)


class TestvEB(unittest.TestCase):
    def setUp(self):
        self.v = veb_tree.vEBTree(5)

    def test_single_item_minimum(self):
        value = random.randint(0, 10000)
        self.v.insert(value)
        self.assertEqual(self.v.minimum(), value)

    def test_multiple_item_minimum(self):
        values = {random.randint(0, 10000) for i in range(0, 10)}
        for v in values:
            self.v.insert(v)
        self.assertEqual(self.v.minimum(), min(values))

    def test_single_item_maximum(self):
        value = random.randint(0, 10000)
        self.v.insert(value)
        self.assertEqual(self.v.maximum(), value)

    def test_multiple_item_maximum(self):
        values = {random.randint(0, 10000) for i in range(0, 10)}
        for v in values:
            self.v.insert(v)
        self.assertEqual(self.v.maximum(), max(values))

    def test_single_item_member(self):
        value = random.randint(0, 100)
        self.v.insert(value)
        for i in range(0, 101):
            if i == value:
                self.assertTrue(self.v.member(i))
            else:
                self.assertFalse((self.v.member(i)))

    def test_multiple_item_member(self):
        values = {random.randint(0, 100) for i in range(0, 10)}
        for v in values:
            self.v.insert(v)
        for i in range(0, 101):
            if i in values:
                self.assertTrue(self.v.member(i))
            else:
                self.assertFalse(self.v.member(i))

    def test_successor(self):
        values = []
        while len(values) < 2:
            values = sorted(list({random.randint(0, 10000) for i in range(0, 100)}))
        for v in values:
            self.v.insert(v)
        index = random.randint(0, len(values)-2)
        self.assertEqual(self.v.successor(values[index]), values[index + 1])

    def test_predecessor(self):
        values = []
        while len(values) < 2:
            values = sorted(list({random.randint(0, 10000) for i in range(0, 100)}))
        for v in values:
            self.v.insert(v)
        index = random.randint(1, len(values)-1)
        self.assertEqual(self.v.predecessor(values[index]), values[index - 1])

    def test_single_item_delete(self):
        value = random.randint(0, 10000)
        self.v.insert(value)
        self.v.delete(value)
        self.assertFalse(self.v.member(value))

    def test_multiple_item_delete(self):
        for i in range(0, 1000):
            self.v.insert(i)
        values_to_delete = {random.randint(0, 999) for i in range(0, 100)}
        for v in values_to_delete:
            self.v.delete(v)
        for i in range(0, 1000):
            if i in values_to_delete:
                self.assertFalse(self.v.member(i))
            else:
                self.assertTrue(self.v.member(i))

    def test_all_item_delete(self):
        for i in range(0, 1000):
            self.v.insert(i)
        for i in range(0, 1000):
            self.v.delete(i)
        for i in range(0, 1000):
            self.assertFalse(self.v.member(i))


if __name__ == 'main':
    unittest.main()