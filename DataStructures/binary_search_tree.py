class BinarySearchTree:
    """ BST implementation. Similar to standard BinaryTree, but operates as a key-value store. """

    class _Node:
        """ Inner class used for a node in the tree. Contains a key, value, and references to left, right and parent """
        def __init__(self, k, v, left=None, right=None, parent=None):
            self.k = k
            self.v = v
            self.l = left
            self.r = right
            self.p = parent

    def __init__(self):
        """ Initialise an empty BST. Complexity: O(1) """
        self.root = None

    def _get_min_child_node_from_node(self, node):
        """ Returns the minimum values node which is a child of node. Called by delete() """
        while not(node.l is None):
            node = node.l
        return node

    def _transplant(self, t, r):
        """ Replaces subtree rooted at t with that rooted at r. Called by delete() """
        if t.p is None:
            self.root = r
        elif t == t.p.l:
            t.p.l = r
        else:
            t.p.r = r
        if not(r is None):
            r.p = t.p

    def contains(self, k):
        """ Returns True if key k is in the tree, otherwise False. Complexity: O(lgn) """
        current_node = self.root
        while not(current_node is None):
            if k < current_node.k:
                current_node = current_node.l
            elif k > current_node.k:
                current_node = current_node.r
            else:
                return True
        return False

    def get(self, k):
        """ Returns the value associated with key k from tree. Complexity: O(lgn) """
        current_node = self.root
        while True:
            if current_node is None:
                raise KeyError("no value associated with key in tree")
            if k < current_node.k:
                current_node = current_node.l
            elif k > current_node.k:
                current_node = current_node.r
            else:
                return current_node.v

    def set(self, k, v):
        """ Sets key k to value v to the tree, adding it if it doesn't already exist. Complexity: O(lgn) """
        if self.root is None:
            self.root = self._Node(k, v)
            return
        current_node = self.root
        while True:
            if k < current_node.k:
                if current_node.l is None:
                    current_node.l = self._Node(k, v)
                    current_node.l.p = current_node
                    return
                else:
                    current_node = current_node.l
            elif k > current_node.k:
                if current_node.r is None:
                    current_node.r = self._Node(k, v)
                    current_node.r.p = current_node
                    return
                else:
                    current_node = current_node.r
            else:
                current_node.v = v
                return

    def delete(self, k):
        """ Removes key k from tree. Complexity: O(lgn) """
        node_to_delete = self.root
        while True:
            if node_to_delete is None:
                raise ValueError("value not in tree")
            if k < node_to_delete.k:
                node_to_delete = node_to_delete.l
            elif k > node_to_delete.k:
                node_to_delete = node_to_delete.r
            else:
                break
        if node_to_delete.l is None:
            self._transplant(node_to_delete, node_to_delete.r)
        elif node_to_delete.r is None:
            self._transplant(node_to_delete, node_to_delete.l)
        else:
            succ_node = self._get_min_child_node_from_node(node_to_delete.r)
            if succ_node.p != node_to_delete:
                self._transplant(succ_node, succ_node.r)
                succ_node.r = node_to_delete.r
                succ_node.r.p = succ_node
            self._transplant(node_to_delete, succ_node)
            succ_node.l = node_to_delete.l
            succ_node.l.p = succ_node