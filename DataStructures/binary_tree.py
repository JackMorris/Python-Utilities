class BinaryTree:
    """ Standard binary tree implementation with support for lookup check , insertion and deletion of items """

    class _Node:
        """ Inner class used for a node in the tree. Contains a value, and references to left, right and parent """
        def __init__(self, v, left=None, right=None, parent=None):
            self.v = v
            self.l = left
            self.r = right
            self.p = parent

    def __init__(self):
        """ Initialise an empty binary tree. Complexity: O(1) """
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

    def contains(self, x):
        """ Returns True if x is in the tree, otherwise False. Complexity: O(lgn) """
        current_node = self.root
        while not(current_node is None):
            if x < current_node.v:
                current_node = current_node.l
            elif x > current_node.v:
                current_node = current_node.r
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
            if x < current_node.v:
                if current_node.l is None:
                    current_node.l = new_node
                    new_node.p = current_node
                    return
                else:
                    current_node = current_node.l
            elif x > current_node.v:
                if current_node.r is None:
                    current_node.r = new_node
                    new_node.p = current_node
                    return
                else:
                    current_node = current_node.r
            else:
                raise ValueError("value already in tree")

    def delete(self, x):
        """ Removes x from tree. Complexity: O(lgn) """
        node_to_delete = self.root
        while True:
            if node_to_delete is None:
                raise ValueError("value not in tree")
            if x < node_to_delete.v:
                node_to_delete = node_to_delete.l
            elif x > node_to_delete.v:
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