class BinarySearchTree:
    """ BST implementation. Similar to standard BinaryTree, but operates as a key-value store. """

    class _Node:
        """ Inner class used for a node in the tree. Contains a key, value, and references to left, right and parent """
        def __init__(self, key, val, left=None, right=None, parent=None):
            self.key = key
            self.val = val
            self.left = left
            self.right = right
            self.parent = parent

    def __init__(self):
        """ Initialise an empty BST. Complexity: O(1) """
        self.root = None

    def _get_min_child_node_from_node(self, node):
        """ Returns the minimum values node which is a child of node. Called by delete() """
        while not(node.left is None):
            node = node.left
        return node

    def _transplant(self, dest_tree, new_tree):
        """ Replaces subtree rooted at dest_tree with that rooted at new_tree. Called by delete() """
        if dest_tree.parent is None:
            self.root = new_tree
        elif dest_tree == dest_tree.parent.left:
            dest_tree.parent.left = new_tree
        else:
            dest_tree.parent.right = new_tree
        if not(new_tree is None):
            new_tree.parent = dest_tree.parent

    def contains(self, key):
        """ Returns True if key is in the tree, otherwise False. Complexity: O(lgn) """
        current_node = self.root
        while not(current_node is None):
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                return True
        return False

    def get(self, key):
        """ Returns the value associated with key from tree. Complexity: O(lgn) """
        current_node = self.root
        while True:
            if current_node is None:
                raise KeyError("no value associated with key in tree")
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                return current_node.val

    def set(self, key, val):
        """ Sets key to value val in the tree, adding it if it doesn't already exist. Complexity: O(lgn) """
        if self.root is None:
            self.root = self._Node(key, val)
            return
        current_node = self.root
        while True:
            if key < current_node.key:
                if current_node.left is None:
                    current_node.left = self._Node(key, val)
                    current_node.left.parent = current_node
                    return
                else:
                    current_node = current_node.left
            elif key > current_node.key:
                if current_node.right is None:
                    current_node.right = self._Node(key, val)
                    current_node.right.parent = current_node
                    return
                else:
                    current_node = current_node.right
            else:
                current_node.val = val
                return

    def delete(self, key):
        """ Removes key from tree. Complexity: O(lgn) """
        node_to_delete = self.root
        while True:
            if node_to_delete is None:
                raise ValueError("value not in tree")
            if key < node_to_delete.key:
                node_to_delete = node_to_delete.left
            elif key > node_to_delete.key:
                node_to_delete = node_to_delete.right
            else:
                break
        if node_to_delete.left is None:
            self._transplant(node_to_delete, node_to_delete.right)
        elif node_to_delete.right is None:
            self._transplant(node_to_delete, node_to_delete.left)
        else:
            succ_node = self._get_min_child_node_from_node(node_to_delete.right)
            if succ_node.parent != node_to_delete:
                self._transplant(succ_node, succ_node.right)
                succ_node.right = node_to_delete.right
                succ_node.right.parent = succ_node
            self._transplant(node_to_delete, succ_node)
            succ_node.left = node_to_delete.left
            succ_node.left.parent = succ_node