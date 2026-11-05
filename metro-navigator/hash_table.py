class Entry:
    """Represents a single entry in the hash table."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """Stores key-value pairs and supports station-to-zone lookups"""
    def __init__(self):
        self.capacity = 8
        self.table = [None] * self.capacity
        self.size = 0
    
    def put(self, key, value):
        if type(key) is not str:
            raise TypeError("Keys must be strings")

        index = self._hash(key)
        current = self.table[index]

        while current != None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_entry = Entry(key, value)
        new_entry.next = self.table[index]
        self.table[index] = new_entry
        self.size += 1

        if self.load_factor() > 0.75:
            old_table = self.table
            self.capacity *= 2
            self.table = [None] * self.capacity

            for head in old_table:
                current = head

                while current != None:
                    index = self._hash(current.key)

                    new_entry = Entry(current.key, current.value)
                    new_entry.next = self.table[index]
                    self.table[index] = new_entry

                    current = current.next
    
    def get(self, key, default=None):
        index = self._hash(key)
        current = self.table[index]

        while current != None:
            if current.key == key:
                return current.value
            current = current.next

        return default

    def remove(self, key):
        index = self._hash(key)
        current = self.table[index]
        previous = None

        while current != None:
            if current.key == key:
                if previous is None:
                    self.table[index] = current.next
                else:
                    previous.next = current.next

                self.size -= 1
                return current.value

            previous = current
            current = current.next

        raise KeyError(key)

    def contains(self, key):
        index = self._hash(key)
        current = self.table[index]

        while current != None:
            if current.key == key:
                return True
            current = current.next

        return False
    
    def __contains__(self, key):
        return self.contains(key)
    
    def keys(self):
        result = []

        for head in self.table:
            current = head

            while current != None:
                result.append(current.key)
                current = current.next

        return result

    def values(self):
        result = []

        for head in self.table:
            current = head

            while current != None:
                result.append(current.value)
                current = current.next

        return result

    def items(self):
        result = []

        for head in self.table:
            current = head

            while current != None:
                result.append((current.key, current.value))
                current = current.next

        return result

    def load_factor(self):
        return self.size / self.capacity

    def _hash(self, key):
        if type(key) is not str:
            raise TypeError("Keys must be strings")

        hash_value = 0

        for i, char in enumerate(key):
            hash_value = (hash_value * 31 + ord(char) * (i + 1)) % self.capacity

        return hash_value

    def __getitem__(self, key):
        index = self._hash(key)
        current = self.table[index]

        while current != None:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __len__(self):
        return self.size
