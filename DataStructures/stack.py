class Stack:
    """ Standard First-In, Last-Out stack implementation """

    def __init__(self):
        """ Initialises an empty stack. Complexity: O(1) """
        self.data = []

    def is_empty(self):
        """ Returns True if the stack contains no elements. Complexity: O(1) """
        return len(self.data) == 0

    def push(self, x):
        """ Pushes an element x onto the stack. Complexity: O(1) """
        self.data.append(x)

    def pop(self):
        """ Returns and removes the element at the head of the stack. Raises IndexError if empty. Complexity: O(1) """
        if self.is_empty():
            raise IndexError("stack empty")
        else:
            return self.data.pop()