import random
import time
import unittest
from linked_list import LinkedList
from linked_stack import Stack, is_balanced

class TestStack(unittest.TestCase):

    def test_ST_01(self):
        stack = Stack()

        self.assertEqual(len(stack), 0)
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.to_list(), [])

        with self.assertRaises(IndexError):
            stack.pop()

        with self.assertRaises(IndexError):
            stack.peek()

    def test_ST_02(self):
        stack = Stack()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.peek(), 3)
        self.assertEqual(len(stack), 3)
        self.assertEqual(stack.to_list(), [3, 2, 1])

    def test_ST_03(self):
        stack = Stack()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

        self.assertTrue(stack.is_empty())

        with self.assertRaises(IndexError):
            stack.pop()

    def test_ST_04(self):
        stack = Stack()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        original_length = len(stack)

        self.assertEqual(stack.peek(), 3)
        self.assertEqual(stack.peek(), 3)
        self.assertEqual(stack.peek(), 3)

        self.assertEqual(len(stack), original_length)

    def test_ST_05(self):
        stack = Stack()

        stack.push("a")
        stack.push("b")

        self.assertEqual(stack.pop(), "b")

        stack.push("c")

        self.assertEqual(stack.pop(), "c")
        self.assertEqual(stack.pop(), "a")

        self.assertTrue(stack.is_empty())

    def test_ST_06(self):
        stack = Stack()

        values = [None, 0, [], ("x",)]

        for value in values:
            stack.push(value)

        self.assertEqual(len(stack), 4)

        self.assertEqual(stack.pop(), ("x",))
        self.assertEqual(stack.pop(), [])
        self.assertEqual(stack.pop(), 0)
        self.assertIsNone(stack.pop())

        self.assertTrue(stack.is_empty())

    def test_ST_07(self):
        stack = Stack()

        stack.push(1)
        stack.push(2)

        stack.clear()

        self.assertEqual(len(stack), 0)
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.to_list(), [])

        stack.push(3)

        self.assertEqual(stack.pop(), 3)

        stack1 = Stack()
        stack2 = Stack()

        stack1.push(10)
        stack2.push(20)

        self.assertEqual(stack1.to_list(), [10])
        self.assertEqual(stack2.to_list(), [20])

        self.assertIsNot(stack1._list, stack2._list)

    def test_ST_08(self):
        stack = Stack()

        self.assertIsInstance(stack._list, LinkedList)

        start = time.perf_counter()

        for i in range(20000):
            stack.push(i)

        for i in range(20000):
            stack.pop()

        elapsed = time.perf_counter() - start

        self.assertEqual(len(stack), 0)
        self.assertLess(elapsed, 1.0)

    def test_ST_09(self):
        true_cases = [
            "",
            "()",
            "([]{})",
            "a(b[c]d)e"
        ]

        false_cases = [
            "(",
            ")(",
            "([)]",
            "((())",
            "}{"
        ]

        for text in true_cases:
            with self.subTest(text=text):
                self.assertTrue(is_balanced(text))

        for text in false_cases:
            with self.subTest(text=text):
                self.assertFalse(is_balanced(text))

        with self.assertRaises(TypeError):
            is_balanced(5)

    def test_ST_10(self):
        random.seed(56)

        stack = Stack()
        model = []

        for _ in range(1000):
            operation = random.choice(["push", "pop"])

            if operation == "push":
                value = random.randint(0, 100)

                stack.push(value)
                model.insert(0, value)

            elif operation == "pop":
                if model:
                    expected = model.pop(0)
                    result = stack.pop()

                    self.assertEqual(result, expected)
                else:
                    with self.assertRaises(IndexError):
                        stack.pop()

        self.assertEqual(stack.to_list(), model)
        self.assertEqual(len(stack), len(model))
        self.assertEqual(stack.is_empty(), len(model) == 0)

if __name__ == "__main__":
    unittest.main()
