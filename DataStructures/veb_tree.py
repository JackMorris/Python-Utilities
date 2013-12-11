class vEBTree:
    """ Implementation of a van Emde Boas Tree; an efficient priority queue for when the key universe size is known.
    Tree can contain any key k, 0 <= k < u """

    def __init__(self, k):
        """ Initialises an empty vEB tree, u = 2**2**k. Complexity: O(1) """
        self.k = k
        self.u = 2**2**k
        self.min = None
        self.max = None
        self.summary = None
        self.cluster = []

    def _high(self, x):
        return int(x/(2**2**(self.k-1)))

    def _low(self, x):
        return x % (2**2**(self.k-1))

    def _index(self, x, y):
        return x * (2**2**(self.k-1)) + y

    def minimum(self):
        """ Return minimum value in vEB tree. Complexity: O(1) """
        return self.min

    def maximum(self):
        """ Return maximum value in vEB tree. Complexity: O(1) """
        return self.max

    def member(self, x):
        """ Returns true if x is a member of the tree, False otherwise. Complexity: O(k) """
        if x == self.min or x == self.max:
            return True
        elif self.u == 2 or self.min is None:
            return False
        else:
            cluster_tree = self.cluster[self._high(x)]
            return cluster_tree.member(self._low(x))

    def successor(self, x):
        """ Return the successor to x from the tree. Complexity: O(k) """
        if self.min is None:
            return None
        elif self.u == 2:
            if x == 0 and self.max == 1:
                return 1
        elif x < self.min:
            return self.min
        else:
            high_x = self._high(x)
            max_low = (self.cluster[high_x]).maximum()
            if not(max_low is None) and self._low(x) < max_low:
                offset = (self.cluster[high_x]).successor(self._low(x))
                return self._index(high_x, offset)
            else:
                succ_cluster = self.summary.successor(high_x)
                if succ_cluster is None:
                    return None
                else:
                    offset = (self.cluster[succ_cluster]).minimum()
                    return self._index(succ_cluster, offset)

    def predecessor(self, x):
        """ Return the predecessor to x from the tree. Complexity: O(k) """
        if self.min is None:
            return None
        elif self.u == 2:
            if x == 1 and self.min == 0:
                return 0
        elif x > self.max:
            return self.max
        else:
            high_x = self._high(x)
            min_low = (self.cluster[high_x]).minimum()
            if not(min_low is None) and self._low(x) > min_low:
                offset = (self.cluster[high_x]).predecessor(self._low(x))
                return self._index(high_x, offset)
            else:
                pred_cluster = self.summary.predecessor(high_x)
                if pred_cluster is None:
                    if not(self.min is None) and x > self.min:
                        return self.min
                    else:
                        return None
                else:
                    offset = (self.cluster[pred_cluster]).maximum()
                    return self._index(pred_cluster, offset)

    def insert(self, x):
        """ Insert x into the tree. Complexity: O(k) """
        if self.min is None:
            self.min = x
            self.max = x
            if self.k > 0:
                self.summary = vEBTree(self.k-1)
                for i in range(0, 2**2**(self.k-1)):
                    self.cluster.append(vEBTree(self.k-1))
        else:
            if x < self.min:
                tmp = x
                x = self.min
                self.min = tmp
            if self.u > 2:
                if (self.cluster[self._high(x)]).minimum() is None:
                    self.summary.insert(self._high(x))
                (self.cluster[self._high(x)]).insert(self._low(x))
            if x > self.max:
                self.max = x

    def delete(self, x):
        """ Deletes x from the tree. Assume x is already a member. Complexity: O(k). """
        if self.min == self.max:
            self.min = None
            self.max = None
            self.cluster = []
            self.summary = None
        elif self.u == 2:
            if x == 0:
                self.min = 1
            else:
                self.min = 0
            self.max = self.min
        else:
            if x == self.min:
                first_cluster = self.summary.min
                x = self._index(first_cluster, (self.cluster[first_cluster]).minimum())
                self.min = x
            (self.cluster[self._high(x)]).delete(self._low(x))
            if (self.cluster[self._high(x)]).minimum() is None:
                self.summary.delete(self._high(x))
                if x == self.max:
                    summary_max = self.summary.max
                    if summary_max is None:
                        self.max = self.min
                    else:
                        self.max = self._index(summary_max, (self.cluster[summary_max]).maximum())
            elif x == self.max:
                self.max = self._index(self._high(x), (self.cluster[self._high(x)]).maximum())
