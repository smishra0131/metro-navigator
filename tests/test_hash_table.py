"""Unit tests for hash_table."""
import random
import time
import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def test_HT_01(self):
        ht = HashTable()
        self.assertEqual(len(ht), 0)
        self.assertEqual(ht.capacity, 8)
        self.assertEqual(ht.keys(), [])
        self.assertFalse(ht.contains("a"))
        self.assertEqual(ht.load_factor(), 0)

def test_HT_02(self):
    ht = HashTable()
    ht.put("a", 1)
    self.assertEqual(ht.get("a"), 1)
    ht["b"] = 2
    self.assertEqual(ht["b"], 2)
    self.assertEqual(len(ht), 2)

def test_HT_03(self):
    ht = HashTable()
    ht.put("a", 1)
    ht.put("a", 99)
    self.assertEqual(ht.get("a"), 99)
    self.assertEqual(len(ht), 1)

def test_HT_04(self):
    ht = HashTable()
    self.assertIsNone(ht.get("zzz"))
    self.assertEqual(ht.get("zzz", 0), 0)
    with self.assertRaises(KeyError):
        ht["zzz"]

def test_HT_05(self):
    ht = HashTable()
    ht.put("a", 1)
    self.assertTrue(ht.contains("a"))
    self.assertTrue("a" in ht)
    self.assertFalse(ht.contains("b"))
    ht.remove("a")
    self.assertFalse(ht.contains("a"))
    self.assertFalse("a" in ht)

def test_HT_06(self):
    ht = HashTable()
    ht.put("a", 10)
    self.assertEqual(ht.remove("a"), 10)
    self.assertEqual(len(ht), 0)
    with self.assertRaises(KeyError):
        ht.remove("a")
    
    ht.put("a", 20)
    self.assertEqual(ht.get("a"), 20)

def test_HT_07(self):
    ht = HashTable()
    result = ht._hash("station")
    self.assertIsInstance(result, int)
    self.assertGreaterEqual(result, 0)
    self.assertLess(result, ht.capacity)
    self.assertEqual(result, ht._hash("station"))
    for i in range(10):
        ht.put("key" + str(i), i)

    self.assertGreater(ht.capacity, 8)
    result = ht._hash("station")
    self.assertGreaterEqual(result, 0)
    self.assertLess(result, ht.capacity)

def test_HT_08(self):
    ht = HashTable()
    collisions = []
    for i in range(100):
        key = "key" + str(i)

        if not collisions:
            collisions.append(key)
        elif ht._hash(key) == ht._hash(collisions[0]):
            collisions.append(key)

        if len(collisions) == 3:
            break

    self.assertEqual(len(collisions), 3)
    for i, key in enumerate(collisions):
        ht.put(key, i)

    self.assertEqual(len(ht), 3)
    self.assertEqual(ht.remove(collisions[0]), 0)
    self.assertEqual(ht.get(collisions[1]), 1)
    self.assertEqual(ht.get(collisions[2]), 2)
    self.assertEqual(ht.remove(collisions[1]), 1)
    self.assertEqual(ht.get(collisions[2]), 2)
    self.assertEqual(ht.remove(collisions[2]), 2)
    self.assertEqual(len(ht), 0)

def test_HT_09(self):
    ht = HashTable()
    ht.put("", 1)
    ht.put("A", 2)
    ht.put("a", 3)
    ht.put("abc", 4)
    ht.put("cba", 5)
    self.assertEqual(ht.get(""), 1)
    self.assertEqual(ht.get("A"), 2)
    self.assertEqual(ht.get("a"), 3)
    self.assertEqual(ht.get("abc"), 4)
    self.assertEqual(ht.get("cba"), 5)
    self.assertEqual(len(ht), 5)

def test_HT_10(self):
    ht = HashTable()
    invalid_keys = [5, None, 3.14, ("a",)]
    for key in invalid_keys:
        with self.subTest(key=key):
            with self.assertRaises(TypeError):
                ht.put(key, 1)

            with self.assertRaises(TypeError):
                ht.get(key)

            with self.assertRaises(TypeError):
                ht.remove(key)

            with self.assertRaises(TypeError):
                ht.contains(key)

def test_HT_11(self):
    ht = HashTable()
    ht.put("a", None)
    ht.put("b", 0)
    ht.put("c", False)
    ht.put("d", [])
    self.assertIsNone(ht.get("a", "default"))
    self.assertEqual(ht.get("b"), 0)
    self.assertIs(ht.get("c"), False)
    self.assertEqual(ht.get("d"), [])
    self.assertTrue(ht.contains("a"))
    self.assertEqual(len(ht), 4)

def test_HT_12(self):
    ht = HashTable()
    for i in range(6):
        ht.put("key" + str(i), i)
    
    self.assertEqual(ht.capacity, 8)
    self.assertEqual(ht.load_factor(), 0.75)
    ht.put("key6", 6)
    self.assertEqual(ht.capacity, 16)
    old_capacity = ht.capacity
    ht.put("key0", 100)
    self.assertEqual(ht.capacity, old_capacity)
    self.assertEqual(ht.get("key0"), 100)

def test_HT_13(self):
    ht = HashTable()
    for i in range(100):
        key = "key" + str(i)
        ht.put(key, i)

        self.assertEqual(ht.get(key), i)
        self.assertLessEqual(ht.load_factor(), 0.75)

    self.assertEqual(len(ht), 100)

def test_HT_14(self):
    ht = HashTable()
    expected = {}
    for i in range(20):
        key = "key" + str(i)
        expected[key] = i
        ht.put(key, i)

    self.assertEqual(len(ht.keys()), 20)
    self.assertEqual(len(ht.values()), 20)
    self.assertEqual(len(ht.items()), 20)
    self.assertEqual(sorted(ht.keys()), sorted(expected.keys()))
    for key, value in ht.items():
        self.assertEqual(ht.get(key), value)

def test_HT_15(self):
    ht = HashTable()
    for i in range(6):
        ht.put("key" + str(i), i)

    self.assertEqual(
        ht.load_factor(),
        len(ht) / ht.capacity
    )
    old_capacity = ht.capacity
    ht.remove("key0")
    ht.remove("key1")
    self.assertEqual(
        ht.load_factor(),
        len(ht) / ht.capacity
    )
    self.assertLessEqual(ht.capacity, old_capacity)

def test_HT_16(self):
    ht = HashTable()
    for i in range(5000):
        ht.put("station_" + str(i), i)

    self.assertEqual(len(ht), 5000)
    for i in range(5000):
        self.assertEqual(ht.get("station_" + str(i)), i)

    for i in range(0, 5000, 2):
        ht.remove("station_" + str(i))

    for i in range(1, 5000, 2):
        self.assertTrue(ht.contains("station_" + str(i)))

    for i in range(0, 5000, 2):
        self.assertFalse(ht.contains("station_" + str(i)))

    self.assertEqual(len(ht), 2500)

def test_HT_17(self):
    random.seed(42)
    ht = HashTable()
    model = {}

    for _ in range(2000):
        operation = random.choice([
            "put",
            "get",
            "remove"
        ])
        key = "key" + str(random.randint(0, 100))
        value = random.randint(0, 1000)
        if operation == "put":
            ht.put(key, value)
            model[key] = value

        elif operation == "get":
            self.assertEqual(
                ht.get(key),
                model.get(key)
            )

        elif operation == "remove":
            if key in model:
                expected = model.pop(key)
                self.assertEqual(ht.remove(key), expected)
            else:
                with self.assertRaises(KeyError):
                    ht.remove(key)

        self.assertEqual(len(ht), len(model))
        for k, v in model.items():
            self.assertEqual(ht.get(k), v)

if __name__ == "__main__":
    unittest.main()