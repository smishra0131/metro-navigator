import unittest
from bst import BST
from graph import Graph
from hash_set import HashSet
from hash_table import HashTable
from linked_list import LinkedList
from linked_queue import Queue
from linked_stack import Stack
from min_heap import MinHeap

class TestIntegration(unittest.TestCase):

    def create_metro_graph(self):
        graph = Graph()
        stations = ["Airport", "Beach", "Campus", "Downtown", "Eastside", "Factory", "Garden"]
        connections = [
            ("Airport", "Downtown"),
            ("Airport", "Eastside"),
            ("Beach", "Campus"),
            ("Beach", "Garden"),
            ("Campus", "Downtown"),
            ("Downtown", "Eastside"),
            ("Downtown", "Factory"),
            ("Eastside", "Factory"),
            ("Factory", "Garden")
        ]

        for station in stations:
            graph.add_vertex(station)

        for u, v in connections:
            graph.add_edge(u, v)

        return graph

    def test_INT_01(self):
        tree = BST()

        stations = [
            "Downtown",
            "Beach",
            "Factory",
            "Airport",
            "Campus",
            "Eastside",
            "Garden"
        ]

        for station in stations:
            tree.insert(station)

        self.assertEqual(
            tree.inorder(),
            [
                "Airport",
                "Beach",
                "Campus",
                "Downtown",
                "Eastside",
                "Factory",
                "Garden"
            ]
        )

        self.assertEqual(tree.height(), 3)
        self.assertEqual(tree.count_leaves(), 4)

        self.assertEqual(
            tree.preorder(),
            ["Downtown", "Beach", "Airport", "Campus", "Factory","Eastside", "Garden"]
        )

    def test_INT_02(self):
        fares = HashTable()
        fare_zones = {
            "Airport": 1,
            "Beach": 3,
            "Campus": 2,
            "Downtown": 1,
            "Eastside": 2,
            "Factory": 2,
            "Garden": 3
        }

        for station, zone in fare_zones.items():
            fares.put(station, zone)

        for station, expected_zone in fare_zones.items():
            with self.subTest(station=station):
                self.assertEqual(
                    fares.get(station),
                    expected_zone
                )

        self.assertEqual(len(fares), 7)

    def test_INT_03(self):
        trip = LinkedList()
        stations = ["Airport", "Downtown", "Campus", "Beach"]
        for station in stations:
            trip.append(station)

        self.assertEqual(
            str(trip),
            "Airport -> Downtown -> Campus -> Beach -> None"
        )

        trip.reverse()
        self.assertEqual(
            str(trip),
            "Beach -> Campus -> Downtown -> Airport -> None"
        )

    def test_INT_04(self):
        heap = MinHeap()
        tasks = [
            (3, "Inspect Beach-Campus sign"),
            (1, "Repair Eastside crossing"),
            (2, "Replace Downtown display")
        ]

        for priority, task in tasks:
            heap.push(priority, task)

        result = [
            heap.pop(),
            heap.pop(),
            heap.pop()
        ]

        self.assertEqual(
            result,
            [
                (1, "Repair Eastside crossing"),
                (2, "Replace Downtown display"),
                (3, "Inspect Beach-Campus sign")
            ]
        )

        self.assertTrue(heap.is_empty())

    def test_INT_05(self):
        graph = self.create_metro_graph()
        airport_neighbors = HashSet()
        factory_neighbors = HashSet()
        for station in graph.neighbors("Airport"):
            airport_neighbors.add(station)

        for station in graph.neighbors("Factory"):
            factory_neighbors.add(station)

        common_stops = airport_neighbors.intersection(
            factory_neighbors
        )

        self.assertEqual(
            sorted(common_stops.to_list()),
            ["Downtown", "Eastside"]
        )

        beach_neighbors = HashSet()
        for station in graph.neighbors("Beach"):
            beach_neighbors.add(station)

        self.assertEqual(
            sorted(airport_neighbors.union(
                beach_neighbors
            ).to_list()),
            ["Campus", "Downtown", "Eastside", "Garden"]
        )

        self.assertEqual(
            sorted(airport_neighbors.intersection(
                beach_neighbors
            ).to_list()),
            []
        )

    def test_INT_06(self):
        stack = Stack()
        pages = ["Airport", "Downtown", "Campus", "Beach"]

        for page in pages:
            stack.push(page)

        self.assertEqual(stack.pop(), "Beach")
        self.assertEqual(stack.pop(), "Campus")
        self.assertEqual(stack.peek(), "Downtown")
        self.assertEqual(
            stack.to_list(),
            ["Downtown", "Airport"]
        )

    def test_INT_07(self):
        queue = Queue()
        passengers = ["Ana", "Ben", "Cy"]
        for passenger in passengers:
            queue.enqueue(passenger)

        self.assertEqual(queue.dequeue(), "Ana")
        self.assertEqual(queue.peek(), "Ben")
        self.assertEqual(len(queue), 2)
        self.assertEqual(
            queue.to_list(),
            ["Ben", "Cy"]
        )

    def test_INT_08(self):
        graph = self.create_metro_graph()
        downtown_neighbors = graph.neighbors("Downtown")
        queue = Queue()
        for station in downtown_neighbors:
            queue.enqueue(station)

        queue_result = []
        while not queue.is_empty():
            queue_result.append(queue.dequeue())

        self.assertEqual(
            queue_result,
            ["Airport", "Campus", "Eastside", "Factory"]
        )

        stack = Stack()
        for station in downtown_neighbors:
            stack.push(station)

        stack_result = []
        while not stack.is_empty():
            stack_result.append(stack.pop())

        self.assertEqual(
            stack_result,
            ["Factory", "Eastside", "Campus", "Airport"]
        )


if __name__ == "__main__":
    unittest.main()