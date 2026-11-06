import random
import time
import unittest
from linked_queue import Queue, board_passengers
from linked_list import LinkedList

class TestQueue(unittest.TestCase):
    def test_QU_01(self):
        queue = Queue()
        self.assertEqual(len(queue), 0)
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.to_list(), [])
        with self.assertRaises(IndexError):
            queue.dequeue()

        with self.assertRaises(IndexError):
            queue.peek()

    def test_QU_02(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(len(queue), 3)
        self.assertEqual(queue.to_list(), [1, 2, 3])

    def test_QU_03(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertTrue(queue.is_empty())
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_QU_04(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        original_length = len(queue)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(queue.peek(), 1)
        self.assertEqual(len(queue), original_length)

    def test_QU_05(self):
        queue = Queue()
        queue.enqueue("a")
        queue.enqueue("b")
        self.assertEqual(queue.dequeue(), "a")
        queue.enqueue("c")
        self.assertEqual(queue.dequeue(), "b")
        self.assertEqual(queue.dequeue(), "c")
        self.assertTrue(queue.is_empty())

    def test_QU_06(self):
        queue = Queue()
        for i in range(5):
            queue.enqueue(1)
            self.assertEqual(queue.dequeue(), 1)
            self.assertTrue(queue.is_empty())
            queue.enqueue(2)
            queue.enqueue(3)
            self.assertEqual(queue.to_list(), [2, 3])
            self.assertEqual(queue.peek(), 2)
            self.assertEqual(queue.dequeue(), 2)
            self.assertEqual(queue.dequeue(), 3)
            self.assertTrue(queue.is_empty())

    def test_QU_07(self):
        queue = Queue()
        values = [None, 0, [], ("x",)]
        for value in values:
            queue.enqueue(value)
        self.assertEqual(len(queue), 4)
        self.assertIsNone(queue.dequeue())
        self.assertEqual(queue.dequeue(), 0)
        self.assertEqual(queue.dequeue(), [])
        self.assertEqual(queue.dequeue(), ("x",))
        self.assertTrue(queue.is_empty())

    def test_QU_08(self):
        queue = Queue()
        self.assertIsInstance(queue._list, LinkedList)
        start = time.perf_counter()
        for i in range(20000):
            queue.enqueue(i)

        for i in range(20000):
            queue.dequeue()

        elapsed = time.perf_counter() - start
        self.assertEqual(len(queue), 0)
        self.assertLess(elapsed, 1.0)

    def test_QU_09(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.clear()
        self.assertEqual(len(queue), 0)
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.to_list(), [])
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 3)
        queue1 = Queue()
        queue2 = Queue()
        queue1.enqueue(10)
        queue2.enqueue(20)
        self.assertEqual(queue1.to_list(), [10])
        self.assertEqual(queue2.to_list(), [20])
        self.assertIsNot(queue1._list, queue2._list)

    def test_QU_10(self):
        names = ["A", "B", "C", "D", "E"]
        result = board_passengers(names, 3)
        self.assertEqual(
            result,
            (["C", "A", "E", "B"], "D")
        )

    def test_QU_11(self):
        names = ["A", "B", "C", "D", "E"]
        result = board_passengers(names, 1)
        self.assertEqual(
            result,
            (["A", "B", "C", "D"], "E")
        )

        names = ["A", "B", "C"]
        result = board_passengers(names, 10)
        self.assertEqual(
            result,
            (["A", "C"], "B")
        )

        names = ["Z"]
        result = board_passengers(names, 3)
        self.assertEqual(result, ([], "Z"))

        names = ["A", "B", "C", "D", "E"]
        original_names = names.copy()
        board_passengers(names, 3)
        self.assertEqual(names, original_names)
        with self.assertRaises(ValueError):
            board_passengers([], 3)

        with self.assertRaises(ValueError):
            board_passengers(["A", "B"], 0)

    def test_QU_12(self):
        random.seed(67)
        queue = Queue()
        model = []
        for _ in range(1000):
            operation = random.choice(["enqueue", "dequeue"])
            if operation == "enqueue":
                value = random.randint(0, 100)

                queue.enqueue(value)
                model.append(value)

            elif operation == "dequeue":
                if model:
                    expected = model.pop(0)
                    result = queue.dequeue()

                    self.assertEqual(result, expected)
                else:
                    with self.assertRaises(IndexError):
                        queue.dequeue()

            self.assertEqual(queue.to_list(), model)
            self.assertEqual(len(queue), len(model))
            self.assertEqual(
                queue.is_empty(),
                len(model) == 0
            )


if __name__ == "__main__":
    unittest.main()
