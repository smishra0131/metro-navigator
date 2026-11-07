import random
import time
import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_LL_01(self):
        ll = LinkedList()
        self.assertEqual(len(ll), 0)
        self.assertTrue(ll.is_empty())
        self.assertEqual(ll.to_list(), [])
        self.assertEqual(str(ll), "None")
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

    def test_LL_02(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(len(ll), 3)
        self.assertEqual(ll.to_list(), [1, 2, 3])
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 3)

    def test_LL_03(self):
        ll = LinkedList()
        ll.prepend(1)
        ll.prepend(2)
        ll.prepend(3)
        self.assertEqual(len(ll), 3)
        self.assertEqual(ll.to_list(), [3, 2, 1])
        self.assertEqual(ll.head.value, 3)
        self.assertEqual(ll.tail.value, 1)

    def test_LL_04(self):
        ll = LinkedList()
        ll.append(5)
        self.assertEqual(ll.head.value, 5)
        self.assertEqual(ll.tail.value, 5)
        ll.prepend(4)
        self.assertEqual(ll.head.value, 4)
        self.assertEqual(ll.tail.value, 5)
        ll.append(6)
        self.assertEqual(ll.head.value, 4)
        self.assertEqual(ll.tail.value, 6)
        self.assertEqual(ll.to_list(), [4, 5, 6])

    def test_LL_05(self):
        ll = LinkedList()
        ll.insert_at(0, 1)
        ll.insert_at(1, 3)
        ll.insert_at(1, 2)
        ll.insert_at(0, 0)
        self.assertEqual(ll.to_list(), [0, 1, 2, 3])

    def test_LL_06(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        original = ll.to_list()
        with self.assertRaises(IndexError):
            ll.insert_at(-1, 5)

        with self.assertRaises(IndexError):
            ll.insert_at(4, 5)

        self.assertEqual(ll.to_list(), original)

    def test_LL_07(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.get(0), 1)
        self.assertEqual(ll.get(1), 2)
        self.assertEqual(ll.get(2), 3)
        with self.assertRaises(IndexError):
            ll.get(3)

        with self.assertRaises(IndexError):
            ll.get(-1)

        empty = LinkedList()
        with self.assertRaises(IndexError):
            empty.get(0)

    def test_LL_08(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(1)
        self.assertEqual(ll.find(1), 0)
        self.assertEqual(ll.find(2), 1)
        self.assertEqual(ll.find(3), -1)
        empty = LinkedList()
        self.assertEqual(empty.find(1), -1)

    def test_LL_09(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(1)
        self.assertTrue(ll.remove(1))
        self.assertEqual(ll.to_list(), [2, 1])
        self.assertEqual(len(ll), 2)

    def test_LL_10(self):
        ll = LinkedList()
        ll.append(1)
        self.assertFalse(ll.remove(2))
        self.assertEqual(ll.to_list(), [1])
        self.assertEqual(len(ll), 1)
        empty = LinkedList()
        self.assertFalse(empty.remove(1))

    def test_LL_11(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertTrue(ll.remove(1))
        self.assertEqual(ll.to_list(), [2, 3])
        self.assertTrue(ll.remove(3))
        self.assertEqual(ll.to_list(), [2])
        ll.append(9)
        self.assertEqual(ll.to_list(), [2, 9])
        self.assertEqual(ll.tail.value, 9)

    def test_LL_12(self):
        ll = LinkedList()
        ll.append(1)
        self.assertTrue(ll.remove(1))
        self.assertEqual(len(ll), 0)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        ll.append(2)
        self.assertEqual(ll.to_list(), [2])

    def test_LL_13(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.remove_at(1), 2)
        self.assertEqual(ll.to_list(), [1, 3])
        self.assertEqual(ll.remove_at(0), 1)
        self.assertEqual(ll.to_list(), [3])
        self.assertEqual(ll.remove_at(0), 3)
        self.assertEqual(len(ll), 0)
        with self.assertRaises(IndexError):
            ll.remove_at(0)

        with self.assertRaises(IndexError):
            ll.remove_at(-1)

    def test_LL_14(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        old_head = ll.head
        old_tail = ll.tail

        ll.reverse()

        self.assertEqual(ll.to_list(), [3, 2, 1])
        self.assertIs(ll.head, old_tail)
        self.assertIs(ll.tail, old_head)

        ll.append(4)
        self.assertEqual(ll.to_list(), [3, 2, 1, 4])

        empty = LinkedList()
        empty.reverse()
        self.assertTrue(empty.is_empty())

        single = LinkedList()
        single.append(1)
        single.reverse()
        self.assertEqual(single.to_list(), [1])

    def test_LL_15(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        self.assertEqual(list(ll), [1, 2, 3])
        self.assertEqual(str(ll), "1 -> 2 -> 3 -> None")

        empty = LinkedList()
        self.assertEqual(list(empty), [])
        self.assertEqual(str(empty), "None")

    def test_LL_16(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)

        ll.clear()

        self.assertEqual(len(ll), 0)
        self.assertTrue(ll.is_empty())
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)

        ll.append(3)
        self.assertEqual(ll.to_list(), [3])

        ll.append(None)
        self.assertEqual(ll.to_list(), [3, None])

        ll1 = LinkedList()
        ll2 = LinkedList()

        ll1.append(10)
        ll2.append(20)

        self.assertEqual(ll1.to_list(), [10])
        self.assertEqual(ll2.to_list(), [20])
        self.assertIsNot(ll1.head, ll2.head)

    def test_LL_17(self):
        ll = LinkedList()

        start = time.perf_counter()

        for i in range(20000):
            ll.append(i)

        elapsed = time.perf_counter() - start

        self.assertEqual(len(ll), 20000)
        self.assertEqual(ll.get(19999), 19999)
        self.assertLess(elapsed, 1.0)

    def test_LL_18(self):
        random.seed(42)

        ll = LinkedList()
        model = []

        for _ in range(1000):
            operation = random.choice([
                "append",
                "prepend",
                "insert_at",
                "remove",
                "remove_at",
                "reverse"
            ])

            if operation == "append":
                value = random.randint(0, 100)
                ll.append(value)
                model.append(value)

            elif operation == "prepend":
                value = random.randint(0, 100)
                ll.prepend(value)
                model.insert(0, value)

            elif operation == "insert_at":
                value = random.randint(0, 100)
                index = random.randint(0, len(model))
                ll.insert_at(index, value)
                model.insert(index, value)

            elif operation == "remove":
                value = random.randint(0, 100)

                expected = value in model
                result = ll.remove(value)

                self.assertEqual(result, expected)
                if expected:
                    model.remove(value)

            elif operation == "remove_at":
                if model:
                    index = random.randrange(len(model))

                    expected = model.pop(index)
                    result = ll.remove_at(index)

                    self.assertEqual(result, expected)

            elif operation == "reverse":
                ll.reverse()
                model.reverse()

            self.assertEqual(ll.to_list(), model)
            self.assertEqual(len(ll), len(model))
            self.assertEqual(list(ll), model)
            if model:
                self.assertEqual(ll.head.value, model[0])
                self.assertEqual(ll.tail.value, model[-1])
            else:
                self.assertIsNone(ll.head)
                self.assertIsNone(ll.tail)

    def test_LL_19(self):
        ll = LinkedList()

        for i in range(20000):
            ll.append(i)

        start = time.perf_counter()
        for i in range(20000):
            self.assertEqual(ll.remove_at(0), i)

        elapsed = time.perf_counter() - start
        self.assertEqual(len(ll), 0)
        self.assertIsNone(ll.head)
        self.assertIsNone(ll.tail)
        self.assertLess(elapsed, 1.0)

if __name__ == "__main__":
    unittest.main()
