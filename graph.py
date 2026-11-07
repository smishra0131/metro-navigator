from hash_table import HashTable
from linked_list import LinkedList

class Edge:
    def __init__(self, to):
        self.to = to

class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adjacency = HashTable()
        self._vertex_count = 0
        self._edge_count = 0

    def add_vertex(self, name):
        if type(name) != str:
            raise TypeError("Vertex name must be a string")

        if name == "":
            raise ValueError("Vertex name cannot be empty")

        if self.has_vertex(name):
            return False

        self.adjacency.put(name, LinkedList())
        self._vertex_count += 1
        return True

    def add_edge(self, u, v):
        if not self.has_vertex(u) or not self.has_vertex(v):
            raise KeyError("Vertex does not exist")

        if u == v:
            raise ValueError("Self-loops are not allowed")

        if self.has_edge(u, v):
            return False

        self.adjacency.get(u).append(Edge(v))
        if not self.directed:
            self.adjacency.get(v).append(Edge(u))

        self._edge_count += 1
        return True

    def remove_edge(self, u, v):
        if not self.has_vertex(u) or not self.has_vertex(v):
            raise KeyError("Vertex does not exist")

        if not self.has_edge(u, v):
            return False

        self._remove_connection(u, v)
        if not self.directed:
            self._remove_connection(v, u)

        self._edge_count -= 1
        return True

    def _remove_connection(self, u, v):
        linked_list = self.adjacency.get(u)
        current = linked_list.head
        while current is not None:
            if current.value.to == v:
                return linked_list.remove(current.value)

            current = current.next
        return False

    def remove_vertex(self, name):
        if not self.has_vertex(name):
            return False

        if self.directed:
            outgoing = self.neighbors(name)

            for neighbor in outgoing:
                self._remove_connection(name, neighbor)
                self._edge_count -= 1

            for vertex in self.vertices():
                if vertex != name and self.has_edge(vertex, name):
                    self._remove_connection(vertex, name)
                    self._edge_count -= 1

        else:
            outgoing = self.neighbors(name)
            for neighbor in outgoing:
                self._remove_connection(neighbor, name)
                self._edge_count -= 1

        self.adjacency.remove(name)
        self._vertex_count -= 1
        return True

    def has_vertex(self, name):
        return self.adjacency.contains(name)

    def has_edge(self, u, v):
        if not self.has_vertex(u) or not self.has_vertex(v):
            return False
        
        current = self.adjacency.get(u).head
        while current is not None:
            if current.value.to == v:
                return True

            current = current.next
        return False

    def neighbors(self, name):
        if not self.has_vertex(name):
            raise KeyError(name)

        result = []
        current = self.adjacency.get(name).head
        while current is not None:
            result.append(current.value.to)
            current = current.next

        return result

    def degree(self, name):
        if not self.has_vertex(name):
            raise KeyError(name)
        return len(self.adjacency.get(name))

    def vertices(self):
        return self.adjacency.keys()

    def edges(self):
        edge_list = []
        for u in self.vertices():
            for v in self.neighbors(u):
                if self.directed or u < v:
                    edge_list.append((u, v))

        return edge_list

    def vertex_count(self):
        return self._vertex_count

    def edge_count(self):
        return self._edge_count

    def __str__(self):
        result = []
        for u in self.vertices():
            neighbors = self.neighbors(u)
            result.append(f"{u}: {neighbors}")

        return "\n".join(result)
