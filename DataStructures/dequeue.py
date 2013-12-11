class DeQueue:
    """ Efficient implementation of a First-In, First-Out queue. """

    def __init__(self):
        """ Initialises an empty queue. Complexity: O(1) """
        self._back_list = []
        self._front_list = []

    def _balance_queue(self):
        """ Moves all elements from back_list to front_list, reversing in process. Complexity: O(n) """
        for i in range(0, len(self._back_list)):
            self._front_list.append(self._back_list.pop())

    def is_empty(self):
        """ Returns True if the queue contains no elements. Complexity: O(1) """
        return len(self._back_list) == 0 and len(self._front_list) == 0

    def dequeue(self):
        """ Returns and removes the item at front of queue. Raises IndexError if empty. Amortized complexity: O(1) """
        if self.is_empty():
            raise IndexError("queue empty")
        else:
            if len(self._front_list) == 0:
                self._balance_queue()
            return self._front_list.pop()

    def enqueue(self, x):
        """ Adds x to the back of the queue by appending to the back list. Amortized complexity: O(1) """
        self._back_list.append(x)