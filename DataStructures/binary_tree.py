class BinaryTree:
    """ Standard binary tree implementation with support for lookup check , insertion and deletion of items """

    class _Node:
        """ Inner class used for a node in the tree. Contains a value, and references to left, right and parent """
        def __init__(self, val, left=None, right=None, parent=None):
            self.val = val
            self.left = left
            self.right = right
            self.parent = parent

    def __init__(self):
        """ Initialise an empty binary tree. Complexity: O(1) """
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

    def contains(self, x):
        """ Returns True if x is in the tree, otherwise False. Complexity: O(lgn) """
        current_node = self.root
        while not(current_node is None):
            if x < current_node.val:
                current_node = current_node.left
            elif x > current_node.val:
                current_node = current_node.right
            else:
                return True
        return False

    def add(self, x):
        """ Adds x to the tree. Complexity: O(lgn) """
        new_node = self._Node(x)
        if self.root is None:
            self.root = new_node
            return
        current_node = self.root
        while True:
            if x < current_node.val:
                if current_node.left is None:
                    current_node.left = new_node
                    new_node.parent = current_node
                    return
                else:
                    current_node = current_node.left
            elif x > current_node.val:
                if current_node.right is None:
                    current_node.right = new_node
                    new_node.parent = current_node
                    return
                else:
                    current_node = current_node.right
            else:
                raise ValueError("value already in tree")

    def delete(self, x):
        """ Removes x from tree. Complexity: O(lgn) """
        node_to_delete = self.root
        while True:
            if node_to_delete is None:
                raise ValueError("value not in tree")
            if x < node_to_delete.val:
                node_to_delete = node_to_delete.left
            elif x > node_to_delete.val:
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