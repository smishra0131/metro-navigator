from hash_table import HashTable

class HashSet:
    """Stores unique strings without promising an order"""
    def __init__(self):
        self._table = HashTable()

    def add(self, item):
        if type(item) is not str:
            raise TypeError("Items must be strings")

        if self.contains(item):
            return False

        self._table.put(item, True)
        return True

    def remove(self, item):
        if type(item) is not str:
            raise TypeError("Items must be strings")

        if not self.contains(item):
            raise KeyError(item)

        self._table.remove(item)

    def discard(self, item):
        if type(item) is not str:
            raise TypeError("Items must be strings")

        if not self.contains(item):
            return False

        self._table.remove(item)
        return True

    def contains(self, item):
        if type(item) is not str:
            raise TypeError("Items must be strings")

        return self._table.contains(item)

    def union(self, other):
        if type(other) is not HashSet:
            raise TypeError("other must be a HashSet")

        result = HashSet()
        for item in self.to_list():
            result.add(item)

        for item in other.to_list():
            result.add(item)

        return result

    def intersection(self, other):
        if type(other) is not HashSet:
            raise TypeError("other must be a HashSet")

        result = HashSet()
        for item in self.to_list():
            if other.contains(item):
                result.add(item)

        return result

    def difference(self, other):
        if type(other) is not HashSet:
            raise TypeError("other must be a HashSet")

        result = HashSet()
        for item in self.to_list():
            if not other.contains(item):
                result.add(item)

        return result

    def symmetric_difference(self, other):
        if type(other) is not HashSet:
            raise TypeError("other must be a HashSet")

        result = HashSet()
        for item in self.to_list():
            if not other.contains(item):
                result.add(item)

        for item in other.to_list():
            if not self.contains(item):
                result.add(item)

        return result

    def is_subset(self, other):
        if type(other) is not HashSet:
            raise TypeError("other must be a HashSet")

        for item in self.to_list():
            if not other.contains(item):
                return False

        return True

    def is_empty(self):
        return len(self) == 0

    def clear(self):
        self._table = HashTable()

    def to_list(self):
        return self._table.keys()

    def __len__(self):
        return len(self._table)

    def __contains__(self, item):
        return self.contains(item)
