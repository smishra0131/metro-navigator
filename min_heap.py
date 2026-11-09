class MinHeap:
    """Priority structure: the pair with the smallest numeric priority is removed first; represents maintenance tasks"""
    def __init__(self):
        self._data = []

    def push(self, priority, item):
        if type(priority) not in (int, float):
            raise TypeError("Priority must be an integer or float")

        self._data.append((priority, item))
        i = len(self._data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if self._data[i][0] < self._data[parent][0]:
                self._data[i], self._data[parent] = (self._data[parent], self._data[i])
                i = parent
            else:
                break

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty heap")

        if len(self._data) == 1:
            return self._data.pop()

        smallest = self._data[0]
        self._data[0] = self._data.pop()
        i = 0
        n = len(self._data)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest_child = i

            if (left < n and
                    self._data[left][0] < self._data[smallest_child][0]):
                smallest_child = left

            if (right < n and
                    self._data[right][0] < self._data[smallest_child][0]):
                smallest_child = right

            if smallest_child == i:
                break

            self._data[i], self._data[smallest_child] = (
                self._data[smallest_child],
                self._data[i]
            )

            i = smallest_child

        return smallest

    def peek(self):
        if self.is_empty():
            raise IndexError("Cannot peek at an empty heap")
        
        return self._data[0]

    @staticmethod
    def build_heap(pairs):
        heap = MinHeap()
        heap._data = list(pairs)
        for priority, item in heap._data:
            if type(priority) not in (int, float):
                raise TypeError("Priority must be an integer or float")

        n = len(heap._data)
        for i in range(n // 2 - 1, -1, -1):
            current = i
            while True:
                left = 2 * current + 1
                right = 2 * current + 2
                smallest_child = current

                if (left < n and
                        heap._data[left][0] <
                        heap._data[smallest_child][0]):
                    smallest_child = left

                if (right < n and
                        heap._data[right][0] <
                        heap._data[smallest_child][0]):
                    smallest_child = right

                if smallest_child == current:
                    break

                heap._data[current], heap._data[smallest_child] = (heap._data[smallest_child], heap._data[current])
                current = smallest_child

        return heap

    def drain(self):
        result = []
        while self._data:
            result.append(self.pop())
        return result

    def to_list(self):
        return self._data.copy()

    def is_valid_heap(self):
        for i in range(len(self._data) // 2):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(self._data) and self._data[i][0] > self._data[left][0]:
                return False
            if right < len(self._data) and self._data[i][0] > self._data[right][0]:
                return False
        return True

    def is_empty(self):
        return not self._data

    def __len__(self):
        return len(self._data)