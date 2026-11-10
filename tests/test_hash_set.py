"""Unit tests for hash_set."""
import random
import time
import unittest
from hash_set import HashSet

class TestHashSet(unittest.TestCase):
    def test_SET_01(self):
        s = HashSet()
        self.assertEqual(len(s), 0)
        self.assertTrue(s.is_empty())
        self.assertEqual(s.to_list(), [])
        self.assertFalse(s.contains("a"))

    def test_SET_02(self):
        s = HashSet()
        self.assertTrue(s.add("a"))
        self.assertFalse(s.add("a"))
        self.assertEqual(len(s), 1)

    def test_SET_03(self):
        s = HashSet()
        s.add("a")
        self.assertTrue(s.contains("a"))
        self.assertTrue("a" in s)
        s.remove("a")
        self.assertFalse(s.contains("a"))
        self.assertFalse("a" in s)
        s.add("")
        self.assertTrue(s.contains(""))
        self.assertTrue("" in s)
        s.add("A")
        s.add("a")
        self.assertTrue(s.contains("A"))
        self.assertTrue(s.contains("a"))
        self.assertEqual(len(s), 3)

    def test_SET_04(self):
        s = HashSet()
        s.add("a")
        original_length = len(s)
        s.remove("a")
        self.assertEqual(len(s), original_length - 1)
        with self.assertRaises(KeyError):
            s.remove("a")

        self.assertTrue(s.discard("b") is False)
        s.add("b")
        self.assertTrue(s.discard("b"))
        self.assertFalse(s.discard("b"))

    def test_SET_05(self):
        s = HashSet()
        invalid_items = [5, None, ("a",)]
        for item in invalid_items:
            with self.subTest(item=item):
                with self.assertRaises(TypeError):
                    s.add(item)

                with self.assertRaises(TypeError):
                    s.remove(item)

                with self.assertRaises(TypeError):
                    s.discard(item)

                with self.assertRaises(TypeError):
                    s.contains(item)

    def test_SET_06(self):
        s1 = HashSet()
        s2 = HashSet()
        for item in ["a", "b", "c"]:
            s1.add(item)

        for item in ["c", "d"]:
            s2.add(item)

        result = s1.union(s2)
        self.assertEqual(set(result.to_list()), {"a", "b", "c", "d"})
        self.assertEqual(set(s1.to_list()), {"a", "b", "c"})
        self.assertEqual(set(s2.to_list()), {"c", "d"})
        empty = HashSet()
        self.assertEqual(set(s1.union(empty).to_list()), {"a", "b", "c"})
        self.assertEqual(len(s1.union(s1)), len(s1))

    def test_SET_07(self):
        s1 = HashSet()
        s2 = HashSet()
        for item in ["a", "b", "c"]:
            s1.add(item)

        for item in ["b", "c", "d"]:
            s2.add(item)

        result = s1.intersection(s2)
        self.assertEqual(set(result.to_list()), {"b", "c"})
        self.assertEqual(set(s1.to_list()), {"a", "b", "c"})
        self.assertEqual(set(s2.to_list()), {"b", "c", "d"})
        s3 = HashSet()
        s3.add("x")
        self.assertTrue(s1.intersection(s3).is_empty())
        empty = HashSet()
        self.assertTrue(s1.intersection(empty).is_empty())
        self.assertTrue(empty.intersection(s1).is_empty())

    def test_SET_08(self):
        s1 = HashSet()
        s2 = HashSet()
        for item in ["a", "b", "c"]:
            s1.add(item)

        for item in ["b", "d"]:
            s2.add(item)

        result1 = s1.difference(s2)
        result2 = s2.difference(s1)
        self.assertEqual(set(result1.to_list()), {"a", "c"})
        self.assertEqual(set(result2.to_list()), {"d"})
        self.assertTrue(s1.difference(s1).is_empty())
        empty = HashSet()
        self.assertEqual(
            set(s1.difference(empty).to_list()),
            {"a", "b", "c"}
        )

    def test_SET_09(self):
        s1 = HashSet()
        s2 = HashSet()
        for item in ["a", "b", "c"]:
            s1.add(item)

        for item in ["b", "c", "d"]:
            s2.add(item)

        result = s1.symmetric_difference(s2)
        self.assertEqual(set(result.to_list()), {"a", "d"})
        self.assertTrue(s1.symmetric_difference(s1).is_empty())

    def test_SET_10(self):
        s1 = HashSet()
        s2 = HashSet()
        for item in ["a", "b"]:
            s1.add(item)

        for item in ["a", "b", "c"]:
            s2.add(item)

        self.assertTrue(s1.is_subset(s2))
        self.assertFalse(s2.is_subset(s1))
        s3 = HashSet()
        s3.add("a")
        s3.add("b")
        self.assertTrue(s1.is_subset(s3))
        self.assertTrue(HashSet().is_subset(s2))
        empty = HashSet()
        self.assertFalse(s1.is_subset(empty))

    def test_SET_11(self):
        s = HashSet()
        invalid_arguments = [
            [],
            "abc",
            None,
            {"a", "b"}
        ]

        for other in invalid_arguments:
            with self.subTest(other=other):
                with self.assertRaises(TypeError):
                    s.union(other)

                with self.assertRaises(TypeError):
                    s.intersection(other)

                with self.assertRaises(TypeError):
                    s.difference(other)

                with self.assertRaises(TypeError):
                    s.symmetric_difference(other)

                with self.assertRaises(TypeError):
                    s.is_subset(other)

    def test_SET_12(self):
        start = time.perf_counter()
        A = HashSet()
        B = HashSet()
        for i in range(3000):
            A.add("item_" + str(i))

        for i in range(2000, 5000):
            B.add("item_" + str(i))

        union_result = A.union(B)
        intersection_result = A.intersection(B)
        difference_result = A.difference(B)
        symmetric_result = A.symmetric_difference(B)
        self.assertEqual(len(union_result), 5000)
        self.assertEqual(len(intersection_result), 1000)
        self.assertEqual(len(difference_result), 2000)
        self.assertEqual(len(symmetric_result), 4000)
        for i in range(3000):
            self.assertFalse(A.add("item_" + str(i)))

        self.assertEqual(len(A), 3000)
        elapsed = time.perf_counter() - start
        self.assertLess(elapsed, 1.0)

    def test_SET_13(self):
        random.seed(28)
        s = HashSet()
        model = set()
        for _ in range(2000):
            operation = random.choice(["add", "remove", "discard"])
            value = random.randint(0, 100)
            item = "item_" + str(value)
            if operation == "add":
                expected = item not in model
                result = s.add(item)
                model.add(item)
                self.assertEqual(result, expected)

            elif operation == "remove":
                if item in model:
                    s.remove(item)
                    model.remove(item)
                else:
                    with self.assertRaises(KeyError):
                        s.remove(item)

            elif operation == "discard":
                expected = item in model
                result = s.discard(item)
                model.discard(item)
                self.assertEqual(result, expected)

            self.assertEqual(
                sorted(s.to_list()),
                sorted(model)
            )
            self.assertEqual(len(s), len(model))

if __name__ == "__main__":
    unittest.main()