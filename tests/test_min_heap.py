"""Unit tests for MinHeap."""
import random
import time
import unittest
from min_heap import MinHeap

class TestMinHeap(unittest.TestCase):

    def test_MH_01(self):
        heap = MinHeap()
        self.assertEqual(len(heap), 0)
        self.assertTrue(heap.is_empty())
        self.assertEqual(heap.to_list(), [])
        self.assertTrue(heap.is_valid_heap())

    def test_MH_02(self):
        heap = MinHeap()
        with self.assertRaises(IndexError):
            heap.pop()

        with self.assertRaises(IndexError):
            heap.peek()

    def test_MH_03(self):
        heap = MinHeap()
        heap.push(4, "x")
        self.assertEqual(heap.peek(), (4, "x"))
        self.assertEqual(len(heap), 1)
        self.assertEqual(heap.pop(), (4, "x"))
        self.assertTrue(heap.is_empty())

    def test_MH_04(self):
        heap = MinHeap()
        for priority in [5, 3, 8, 1]:
            heap.push(priority, str(priority))

        self.assertEqual(
            [pair[0] for pair in heap.to_list()],
            [1, 3, 8, 5]
        )

    def test_MH_05(self):
        heap = MinHeap()
        pairs = [
            (5, "a"),
            (3, "b"),
            (8, "c"),
            (1, "d"),
            (9, "e"),
            (2, "f"),
            (7, "g")
        ]

        for priority, item in pairs:
            heap.push(priority, item)

        result = [heap.pop() for _ in range(7)]
        self.assertEqual(
            [pair[0] for pair in result],
            [1, 2, 3, 5, 7, 8, 9]
        )

        self.assertEqual(set(result), set(pairs))

    def test_MH_06(self):
        heap = MinHeap()
        for priority in [5, 3, 8, 1]:
            heap.push(priority, str(priority))

        self.assertEqual(heap.pop()[0], 1)
        self.assertEqual(
            [pair[0] for pair in heap.to_list()],
            [3, 5, 8]
        )

    def test_MH_07(self):
        pairs = [
            (1, "a"),
            (5, "b"),
            (2, "c"),
            (6, "d"),
            (7, "e"),
            (3, "f"),
            (4, "g")
        ]

        heap = MinHeap.build_heap(pairs)
        self.assertTrue(heap.is_valid_heap())
        self.assertEqual(heap.pop()[0], 1)
        self.assertEqual(
            [pair[0] for pair in heap.to_list()],
            [2, 5, 3, 6, 7, 4]
        )

        self.assertTrue(heap.is_valid_heap())

    def test_MH_08(self):
        heap = MinHeap()
        for item in ["a", "b", "c", "d", "e"]:
            heap.push(5, item)

        result = heap.drain()
        self.assertEqual(len(result), 5)
        self.assertEqual(
            sorted(item for priority, item in result),
            ["a", "b", "c", "d", "e"]
        )

    def test_MH_09(self):
        heap = MinHeap()
        heap.push(5, {"name": "first"})
        heap.push(5, {"name": "second"})
        first = heap.pop()
        second = heap.pop()
        self.assertEqual(first[0], 5)
        self.assertEqual(second[0], 5)
        self.assertEqual(
            {first[1]["name"], second[1]["name"]},
            {"first", "second"}
        )

    def test_MH_10(self):
        heap = MinHeap()
        pairs = [
            (-3, "a"),
            (0, "b"),
            (0.5, None),
            (2, "d"),
            (2.5, "e")
        ]

        for priority, item in pairs:
            heap.push(priority, item)

        result = heap.drain()
        self.assertEqual(
            [pair[0] for pair in result],
            [-3, 0, 0.5, 2, 2.5]
        )

        self.assertIn((0.5, None), result)

    def test_MH_11(self):
        pairs = [
            (5, "a"),
            (4, "b"),
            (3, "c"),
            (2, "d"),
            (1, "e")
        ]

        original = pairs.copy()
        heap = MinHeap.build_heap(pairs)
        self.assertEqual(
            [pair[0] for pair in heap.to_list()],
            [1, 2, 3, 5, 4]
        )
        self.assertTrue(heap.is_valid_heap())
        self.assertEqual(pairs, original)

    def test_MH_12(self):
        empty = MinHeap.build_heap([])
        self.assertTrue(empty.is_empty())
        heap = MinHeap.build_heap([(4, "a")])
        self.assertEqual(heap.peek(), (4, "a"))
        self.assertEqual(heap.pop(), (4, "a"))
        heap.push(2, "b")
        self.assertEqual(heap.pop(), (2, "b"))

    def test_MH_13(self):
        random.seed(42)
        heap = MinHeap()
        for i in range(200):
            heap.push(random.randint(0, 1000), str(i))
            self.assertTrue(heap.is_valid_heap())

            if random.choice([True, False]) and not heap.is_empty():
                heap.pop()
                self.assertTrue(heap.is_valid_heap())

        test_heap = MinHeap()
        for priority in [1, 2, 3, 4, 5]:
            test_heap.push(priority, str(priority))

        test_heap._data[0] = (99, "changed")
        self.assertFalse(test_heap.is_valid_heap())

    def test_MH_14(self):
        heap = MinHeap()
        pairs = [
            (5, "a"),
            (1, "b"),
            (3, "c"),
            (2, "d")
        ]

        for priority, item in pairs:
            heap.push(priority, item)

        result = heap.drain()
        self.assertEqual(
            [pair[0] for pair in result],
            [1, 2, 3, 5]
        )

        self.assertTrue(heap.is_empty())
        self.assertEqual(heap.drain(), [])

    def test_MH_15(self):
        random.seed(42)
        heap = MinHeap()
        priorities = [
            random.randint(0, 10000)
            for _ in range(1000)
        ]

        for priority in priorities:
            heap.push(priority, str(priority))

        result = heap.drain()
        self.assertEqual(
            [pair[0] for pair in result],
            sorted(priorities)
        )

    def test_MH_16(self):
        heap = MinHeap()
        heap.push(5, "a")
        heap.push(1, "b")
        self.assertEqual(heap.pop()[0], 1)
        heap.push(0, "c")
        heap.push(7, "d")
        self.assertEqual(heap.pop()[0], 0)
        self.assertEqual(heap.pop()[0], 5)
        self.assertEqual(heap.pop()[0], 7)
        self.assertTrue(heap.is_empty())

    def test_MH_17(self):
        random.seed(42)
        heap = MinHeap()
        start = time.perf_counter()
        priorities = [
            random.randint(0, 100000)
            for _ in range(50000)
        ]
        for priority in priorities:
            heap.push(priority, priority)

        for _ in range(50000):
            heap.pop()

        elapsed = time.perf_counter() - start
        self.assertTrue(heap.is_empty())
        self.assertLess(elapsed, 2.0)

    def test_MH_18(self):
        random.seed(93)
        heap = MinHeap()
        model = []
        for i in range(2000):
            if not model or random.choice(["push", "push", "pop"]) == "push":
                priority = random.randint(-100, 1000)
                item = "item_" + str(i)
                heap.push(priority, item)
                model.append((priority, item))

            else:
                result = heap.pop()
                minimum_priority = min(pair[0] for pair in model)
                self.assertEqual(result[0], minimum_priority)
                model.remove(result)

            self.assertTrue(heap.is_valid_heap())
            self.assertEqual(len(heap), len(model))

    def test_MH_19(self):
        heap = MinHeap()
        heap.push(5, "a")
        heap.push(2, "b")
        heap.push(8, "c")
        original = heap.to_list().copy()
        self.assertEqual(heap.peek(), (2, "b"))
        self.assertEqual(heap.to_list(), original)
        returned_list = heap.to_list()
        returned_list.clear()
        self.assertEqual(heap.to_list(), original)
        self.assertEqual(len(heap), 3)


if __name__ == "__main__":
    unittest.main()
