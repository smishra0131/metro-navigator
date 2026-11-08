import random
import time
import unittest
from graph import Graph

class TestGraph(unittest.TestCase):
    def create_reference_graph(self, directed=False):
        graph = Graph(directed)
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

    def test_G_01(self):
        graph = Graph()
        self.assertEqual(graph.vertex_count(), 0)
        self.assertEqual(graph.edge_count(), 0)
        self.assertEqual(graph.vertices(), [])
        self.assertEqual(graph.edges(), [])

    def test_G_02(self):
        graph = Graph()
        self.assertTrue(graph.add_vertex("A"))
        self.assertFalse(graph.add_vertex("A"))
        self.assertEqual(graph.vertex_count(), 1)
        self.assertTrue(graph.has_vertex("A"))
        self.assertFalse(graph.has_vertex("B"))

    def test_G_03(self):
        graph = Graph()
        with self.assertRaises(TypeError):
            graph.add_vertex(5)

        with self.assertRaises(ValueError):
            graph.add_vertex("")

    def test_G_04(self):
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        self.assertTrue(graph.add_edge("A", "B"))
        self.assertTrue(graph.has_edge("A", "B"))
        self.assertTrue(graph.has_edge("B", "A"))
        self.assertEqual(graph.degree("A"), 1)
        self.assertEqual(graph.degree("B"), 1)
        self.assertEqual(graph.edge_count(), 1)

    def test_G_05(self):
        graph = Graph()
        graph.add_vertex("A")
        with self.assertRaises(KeyError):
            graph.add_edge("A", "B")

        with self.assertRaises(KeyError):
            graph.add_edge("B", "A")

        self.assertEqual(graph.vertex_count(), 1)
        self.assertEqual(graph.edge_count(), 0)

    def test_G_06(self):
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        with self.assertRaises(ValueError):
            graph.add_edge("A", "A")

        self.assertTrue(graph.add_edge("A", "B"))
        self.assertFalse(graph.add_edge("A", "B"))
        self.assertFalse(graph.add_edge("B", "A"))
        self.assertEqual(graph.neighbors("A"), ["B"])
        self.assertEqual(graph.edge_count(), 1)

    def test_G_07(self):
        graph = Graph(directed=True)
        graph.add_vertex("A")
        graph.add_vertex("B")
        self.assertTrue(graph.add_edge("A", "B"))
        self.assertTrue(graph.has_edge("A", "B"))
        self.assertFalse(graph.has_edge("B", "A"))
        self.assertTrue(graph.add_edge("B", "A"))
        self.assertEqual(graph.edge_count(), 2)

    def test_G_08(self):
        graph = Graph()
        for vertex in ["A", "B", "C", "D"]:
            graph.add_vertex(vertex)

        graph.add_edge("A", "C")
        graph.add_edge("A", "B")
        graph.add_edge("A", "D")
        self.assertEqual(
            graph.neighbors("A"),
            ["C", "B", "D"]
        )

        result = graph.neighbors("A")
        result.append("X")
        self.assertEqual(
            graph.neighbors("A"),
            ["C", "B", "D"]
        )

    def test_G_09(self):
        graph = Graph()
        graph.add_vertex("A")
        self.assertEqual(graph.neighbors("A"), [])
        self.assertEqual(graph.degree("A"), 0)
        with self.assertRaises(KeyError):
            graph.neighbors("B")

        with self.assertRaises(KeyError):
            graph.degree("B")

    def test_G_10(self):
        graph = Graph()
        for vertex in ["A", "B", "C"]:
            graph.add_vertex(vertex)

        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        self.assertTrue(graph.remove_edge("A", "B"))
        self.assertFalse(graph.has_edge("A", "B"))
        self.assertFalse(graph.has_edge("B", "A"))
        self.assertTrue(graph.has_edge("A", "C"))
        self.assertEqual(graph.edge_count(), 1)
        self.assertEqual(graph.vertex_count(), 3)
        self.assertFalse(graph.remove_edge("A", "B"))

    def test_G_11(self):
        graph = Graph(directed=True)
        graph.add_vertex("A")
        graph.add_vertex("B")
        graph.add_edge("A", "B")
        graph.add_edge("B", "A")
        self.assertTrue(graph.remove_edge("A", "B"))
        self.assertFalse(graph.has_edge("A", "B"))
        self.assertTrue(graph.has_edge("B", "A"))
        self.assertEqual(graph.edge_count(), 1)

    def test_G_12(self):
        graph = Graph()
        graph.add_vertex("A")
        graph.add_vertex("B")
        with self.assertRaises(KeyError):
            graph.remove_edge("A", "C")

        self.assertFalse(graph.remove_edge("A", "B"))

    def test_G_13(self):
        graph = Graph()
        for vertex in ["A", "B", "C"]:
            graph.add_vertex(vertex)

        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("A", "C")
        self.assertTrue(graph.remove_vertex("B"))
        self.assertEqual(graph.vertex_count(), 2)
        self.assertEqual(graph.edge_count(), 1)
        self.assertEqual(graph.neighbors("A"), ["C"])
        self.assertEqual(graph.neighbors("C"), ["A"])
        self.assertFalse(graph.remove_vertex("B"))
        graph.add_vertex("B")
        self.assertEqual(graph.neighbors("B"), [])

    def test_G_14(self):
        graph = Graph(directed=True)
        for vertex in ["A", "B", "C"]:
            graph.add_vertex(vertex)

        graph.add_edge("A", "B")
        graph.add_edge("B", "C")
        graph.add_edge("C", "B")
        self.assertTrue(graph.remove_vertex("B"))
        self.assertEqual(graph.edge_count(), 0)
        self.assertEqual(graph.neighbors("A"), [])
        self.assertEqual(graph.neighbors("C"), [])

    def test_G_15(self):
        graph = Graph()
        for vertex in ["A", "B", "C"]:
            graph.add_vertex(vertex)

        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "C")
        self.assertEqual(
            sorted(graph.edges()),
            [("A", "B"), ("A", "C"), ("B", "C")]
        )

        directed = Graph(directed=True)
        for vertex in ["A", "B"]:
            directed.add_vertex(vertex)

        directed.add_edge("A", "B")
        directed.add_edge("B", "A")
        self.assertEqual(
            set(directed.edges()),
            {("A", "B"), ("B", "A")}
        )

    def test_G_16(self):
        graph = Graph()
        graph.add_vertex("A")
        self.assertFalse(graph.has_edge("A", "B"))
        self.assertFalse(graph.has_edge("B", "A"))
        self.assertFalse(graph.has_edge("X", "Y"))

    def test_G_17(self):
        graph = Graph()
        graph.add_vertex("Center")
        for i in range(5):
            leaf = "Leaf" + str(i)
            graph.add_vertex(leaf)
            graph.add_edge("Center", leaf)

        self.assertEqual(graph.degree("Center"), 5)
        for i in range(5):
            self.assertEqual(
                graph.degree("Leaf" + str(i)),
                1
            )

        directed = Graph(directed=True)
        for vertex in ["A", "B", "C"]:
            directed.add_vertex(vertex)

        directed.add_edge("A", "B")
        directed.add_edge("A", "C")
        self.assertEqual(directed.degree("A"), 2)
        self.assertEqual(directed.degree("B"), 0)

    def test_G_18(self):
        graph = self.create_reference_graph()
        self.assertEqual(graph.vertex_count(), 7)
        self.assertEqual(graph.edge_count(), 9)
        expected_degrees = {
            "Airport": 2,
            "Beach": 2,
            "Campus": 2,
            "Downtown": 4,
            "Eastside": 3,
            "Factory": 3,
            "Garden": 2
        }

        for station, expected in expected_degrees.items():
            self.assertEqual(
                graph.degree(station),
                expected
            )

        self.assertEqual(
            sum(graph.degree(v) for v in graph.vertices()),
            18
        )

        for u, v in graph.edges():
            self.assertTrue(graph.has_edge(u, v))
            self.assertTrue(graph.has_edge(v, u))

    def test_G_19(self):
        start = time.perf_counter()
        graph = Graph()
        for i in range(1000):
            graph.add_vertex("v" + str(i))

        for i in range(999):
            graph.add_edge(
                "v" + str(i),
                "v" + str(i + 1)
            )

        self.assertEqual(graph.vertex_count(), 1000)
        self.assertEqual(graph.edge_count(), 999)
        for i in range(0, 1000, 2):
            graph.remove_vertex("v" + str(i))

        self.assertEqual(graph.vertex_count(), 500)
        self.assertEqual(graph.edge_count(), 0)
        complete = Graph()
        for i in range(60):
            complete.add_vertex("v" + str(i))

        vertices = complete.vertices()
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                complete.add_edge(vertices[i], vertices[j])

        self.assertEqual(complete.edge_count(), 1770)
        for vertex in vertices:
            self.assertEqual(complete.degree(vertex), 59)

        elapsed = time.perf_counter() - start
        self.assertLess(elapsed, 2.0)

    def test_G_20(self):
        random.seed(49)
        graph = Graph()
        model = {}
        for operation_number in range(1500):
            operation = random.choice([
                "add_vertex",
                "remove_vertex",
                "add_edge",
                "remove_edge"
            ])

            u = "v" + str(random.randint(0, 30))
            v = "v" + str(random.randint(0, 30))
            if operation == "add_vertex":
                result = graph.add_vertex(u)
                if u in model:
                    self.assertFalse(result)
                else:
                    self.assertTrue(result)
                    model[u] = []

            elif operation == "remove_vertex":
                result = graph.remove_vertex(u)
                if u not in model:
                    self.assertFalse(result)
                else:
                    self.assertTrue(result)
                    del model[u]
                    for vertex in model:
                        if u in model[vertex]:
                            model[vertex].remove(u)

            elif operation == "add_edge":
                if u in model and v in model and u != v:
                    result = graph.add_edge(u, v)
                    if v in model[u]:
                        self.assertFalse(result)
                    else:
                        self.assertTrue(result)

                        model[u].append(v)
                        model[v].append(u)

            elif operation == "remove_edge":
                if u in model and v in model:
                    result = graph.remove_edge(u, v)
                    if v in model[u]:
                        self.assertTrue(result)
                        model[u].remove(v)
                        model[v].remove(u)
                    else:
                        self.assertFalse(result)

            if operation_number % 50 == 0:
                self.assertEqual(
                    set(graph.vertices()),
                    set(model.keys())
                )

                expected_edges = set()
                for vertex in model:
                    for neighbor in model[vertex]:
                        if vertex < neighbor:
                            expected_edges.add(
                                (vertex, neighbor)
                            )

                self.assertEqual(
                    set(graph.edges()),
                    expected_edges
                )

                self.assertEqual(
                    graph.edge_count(),
                    len(expected_edges)
                )

                for vertex in model:
                    self.assertEqual(
                        set(graph.neighbors(vertex)),
                        set(model[vertex])
                    )

                    for neighbor in model[vertex]:
                        self.assertTrue(
                            graph.has_edge(vertex, neighbor)
                        )


if __name__ == "__main__":
    unittest.main()