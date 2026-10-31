class Node:
    """Represents a single node in a linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        self.head = None
        self.tail = None
        

    def append(self, value):
        """Add value to the end. Use tail so the method does not traverse existing nodes."""
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        """Add value to the front."""
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_at(self, index, value):
        """Insert so the new value ends up at index. Valid indexes are 0 through len, inclusive; otherwise raise IndexError."""
        if index < 0 or index > len(self):
            raise IndexError("Index out of range")
        if index == 0:
            self.prepend(value)
            return
        if index == len(self):
            self.append(value)
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        new_node = Node(value)
        new_node.next = current.next
        current.next = new_node

    def get(self, index):
        """Return the value at index. Valid indexes are 0 through len - 1. Negative indexes are invalid and raise IndexError."""
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current = self.head
        for i in range(index):
            current = current.next
        return current.value

    def find(self, value):
        """Return the index of the first node whose value == value, or -1 if it is not found."""
        current = self.head
        index = 0
        while current != None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def remove(self, value):
        """Remove the first matching value. Return True if removed and False if not found."""
        if self.head == None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            return True
        current = self.head
        while current.next != None:
            if current.next.value == value:
                current.next = current.next.next
                if current.next == None:
                    self.tail = current
                return True
            current = current.next
        return False

    def remove_at(self, index):
        """Remove the node at index and return its value. Raise IndexError for an invalid index. Removing index 0 must not traverse the list."""
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            if self.head == None:
                self.tail = None
            return value
        current = self.head
        for i in range(index - 1):
            current = current.next
        value = current.next.value
        current.next = current.next.next
        if current.next == None:
            self.tail = current
        return value

    def reverse(self):
        """Reverse in place by changing links. Do not create replacement nodes."""
        prev = None
        current = self.head
        self.tail = self.head
        while current != None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def clear(self):
        """Clear all items"""
        self.head = None
        self.tail = None

    def is_empty(self):
        """Report whether the list is empty"""
        return self.head == None

    def to_list(self):
        """Return a new Python list of values from head to tail."""
        result = []
        current = self.head
        while current != None:
            result.append(current.value)
            current = current.next
        return result

    def __len__(self):
        """Support len(ll)"""
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        """Support iteration with for x in ll, and list(ll)"""
        pass

    
    
    def __str__(self):
        """Return '1 -> 2 -> 3 -> None'. An empty list returns 'None'."""
        if self.head == None:
            return "None"
        result = []
        current = self.head
        while current != None:
            result.append(str(current.value))
            current = current.next
        return " -> ".join(result) + " -> None"