from linked_list import LinkedList

class Queue:
    def __init__(self):
        self._list = LinkedList()

    def enqueue(self, item):
        self._list.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._list.remove_at(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._list.head.value

    def is_empty(self):
        return len(self._list) == 0

    def clear(self):
        self._list.clear()

    def to_list(self):
        return self._list.to_list()

    def __len__(self):
        return len(self._list)



def board_passengers(names, k):
    if type(names) is not list:
        raise TypeError("names must be a list")

    if not all(type(name) is str for name in names):
        raise TypeError("all names must be strings")

    if type(k) is not int:
        raise TypeError("k must be an integer")

    if len(names) == 0:
        raise ValueError("names cannot be empty")

    if k < 1:
        raise ValueError("k must be at least 1")

    queue = Queue()
    for name in names:
        queue.enqueue(name)

    elimination_order = []

    while len(queue) > 1:
        for i in range(k - 1):
            queue.enqueue(queue.dequeue())

        elimination_order.append(queue.dequeue())

    winner = queue.dequeue()
    return (elimination_order, winner)

