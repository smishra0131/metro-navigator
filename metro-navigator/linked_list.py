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
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insert_at(self, index, value):
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
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current = self.head
        for i in range(index):
            current = current.next
        return current.value

    def find(self, value):
        current = self.head
        index = 0
        while current != None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def remove(self, value):
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
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head == None

    def to_list(self):
        result = []
        current = self.head
        while current != None:
            result.append(current.value)
            current = current.next
        return result

    def __len__(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        result = []
        current = self.head

        while current is not None:
            result.append(current.value)
            current = current.next

        return iter(result)

    
    
    def __str__(self):
        if self.head == None:
            return "None"
        result = []
        current = self.head
        while current != None:
            result.append(str(current.value))
            current = current.next
        return " -> ".join(result) + " -> None"