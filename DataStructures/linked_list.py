class LinkedList:
    """ Singly linked list implementation supporting the main Java.util.List operations """

    class _Item:
        """ Inner class used to hold a single item in the list. Contains a value and a reference to the next item """
        def __init__(self, v):
            self.v = v
            self.next = None

    def __init__(self):
        """ Initialises an empty list. Complexity: O(1) """
        self.head = None

    def _get_item_at_index(self, index):
        """ Returns the _Item object at the specified index, throws exception if out of bounds. Complexity: O(n) """
        if index < 0:
            raise IndexError("index out of bounds")
        current_item = self.head
        while True:
            if current_item is None:
                raise IndexError("index out of bounds")
            if index == 0:
                break
            else:
                current_item = current_item.next
                index -= 1
        return current_item

    def is_empty(self):
        """ Returns True if the list contains no elements, False otherwise. Complexity: O(1) """
        return self.head is None

    def contains(self, x):
        """ Returns True if x is in the list, False otherwise. Complexity: O(n) """
        current_item = self.head
        while not(current_item is None):
            if current_item.v == x:
                return True
            current_item = current_item.next
        return False

    def get(self, index):
        """ Gets the item at index, raises IndexError if out of bounds. Complexity: O(n) """
        item = self._get_item_at_index(index)
        return item.v

    def append(self, x):
        """ Adds x to the end of the list. Complexity: O(n) """
        new_item = self._Item(x)
        if self.is_empty():
            self.head = new_item
        else:
            current_item = self.head
            while not(current_item.next is None):
                current_item = current_item.next
            current_item.next = new_item

    def add(self, x, index):
        """ Adds x at the specified index, moving items to the right if not at the end of the list. Complexity: O(n) """
        new_item = self._Item(x)
        if index == 0:
            new_item.next = self.head
            self.head = new_item
        else:
            item = self._get_item_at_index(index-1)
            new_item.next = item.next
            item.next = new_item

    def set(self, x, index):
        """ Sets the value at index to x. Complexity: O(n) """
        item = self._get_item_at_index(index)
        item.v = x

    def delete(self, index):
        """ Removes the value at index. Complexity: O(n) """
        if self.head is None:
            raise IndexError("index out of bounds")
        if index == 0:
            self.head = self.head.next
        else:
            item = self._get_item_at_index(index-1)
            if item.next is None:
                raise IndexError("index out of bounds")
            item.next = item.next.next