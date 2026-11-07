import random
import unittest
from bst import BST

class TestBST(unittest.TestCase):
    def create_reference_tree(self):
        tree = BST()
        for key in [50, 30, 70, 20, 40, 60, 80]:
            tree.insert(key, str(key))
        
        return tree
    
    def test_BST_01(self):
        tree = BST()
        self.assertEqual(len(tree), 0)
        self.assertTrue(tree.is_empty())
        self.assertEqual(tree.height(), 0)
        self.assertEqual(tree.count_leaves(), 0)
        self.assertEqual(tree.inorder(), [])
        self.assertEqual(tree.preorder(), [])
        self.assertEqual(tree.postorder(), [])
        self.assertEqual(tree.level_order(), [])
        self.assertFalse(tree.contains(1))
        self.assertIsNone(tree.root)

    def test_BST_02(self):
        tree = BST()
        with self.assertRaises(ValueError):
            tree.min_key()

        with self.assertRaises(ValueError):
            tree.max_key()

    def test_BST_03(self):
        tree = BST()
        tree.insert(10, "value")
        self.assertEqual(len(tree), 1)
        self.assertEqual(tree.height(), 1)
        self.assertEqual(tree.count_leaves(), 1)
        self.assertEqual(tree.min_key(), 10)
        self.assertEqual(tree.max_key(), 10)

    def test_BST_04(self):
        tree = self.create_reference_tree()
        self.assertEqual(
            tree.inorder(),
            [20, 30, 40, 50, 60, 70, 80]
        )

        self.assertEqual(
            tree.preorder(),
            [50, 30, 20, 40, 70, 60, 80]
        )

        self.assertEqual(
            tree.postorder(),
            [20, 40, 30, 60, 80, 70, 50]
        )

        self.assertEqual(
            tree.level_order(),
            [50, 30, 70, 20, 40, 60, 80]
        )

        self.assertEqual(tree.height(), 3)
        self.assertEqual(tree.count_leaves(), 4)
        self.assertEqual(len(tree), 7)

    def test_BST_05(self):
        tree = BST()

        tree.insert(50, "a")
        tree.insert(50, "b")

        self.assertEqual(len(tree), 1)
        self.assertEqual(tree.get(50), "b")

    def test_BST_06(self):
        tree = self.create_reference_tree()
        for key in [20, 30, 40, 50, 60, 70, 80]:
            with self.subTest(key=key):
                self.assertTrue(tree.contains(key))

        for key in [10, 55, 100]:
            with self.subTest(key=key):
                self.assertFalse(tree.contains(key))

        with self.assertRaises(KeyError):
            tree.get(99)

    def test_BST_07(self):
        ascending = BST()
        for key in range(1, 501):
            ascending.insert(key)

        self.assertEqual(len(ascending), 500)
        self.assertEqual(ascending.height(), 500)
        self.assertEqual(ascending.inorder(), list(range(1, 501)))
        self.assertTrue(ascending.is_valid_bst())

        descending = BST()
        for key in range(500, 0, -1):
            descending.insert(key)

        self.assertEqual(len(descending), 500)
        self.assertEqual(descending.height(), 500)
        self.assertEqual(descending.inorder(), list(range(1, 501)))
        self.assertTrue(descending.is_valid_bst())

    def test_BST_08(self):
        tree = self.create_reference_tree()
        self.assertEqual(tree.min_key(), 20)
        self.assertEqual(tree.max_key(), 80)
        tree.delete(20)
        tree.delete(80)
        self.assertEqual(tree.min_key(), 30)
        self.assertEqual(tree.max_key(), 70)

    def test_BST_09(self):
        tree = self.create_reference_tree()
        self.assertTrue(tree.delete(20))
        self.assertEqual(
            tree.inorder(),
            [30, 40, 50, 60, 70, 80]
        )

        self.assertEqual(len(tree), 6)

    def test_BST_10(self):
        left_tree = BST()
        for key in [50, 30, 70, 20]:
            left_tree.insert(key)

        self.assertTrue(left_tree.delete(30))
        self.assertEqual(left_tree.inorder(), [20, 50, 70])
        self.assertEqual(left_tree.root.left.key, 20)
        right_tree = BST()
        for key in [50, 30, 70, 80]:
            right_tree.insert(key)

        self.assertTrue(right_tree.delete(70))
        self.assertEqual(right_tree.inorder(), [30, 50, 80])
        self.assertEqual(right_tree.root.right.key, 80)

    def test_BST_11(self):
        tree = self.create_reference_tree()
        self.assertTrue(tree.delete(70))
        self.assertEqual(
            tree.preorder(),
            [50, 30, 20, 40, 80, 60]
        )

        self.assertEqual(
            tree.inorder(),
            [20, 30, 40, 50, 60, 80]
        )

    def test_BST_12(self):
        tree = self.create_reference_tree()
        self.assertTrue(tree.delete(50))
        self.assertEqual(tree.root.key, 60)
        self.assertEqual(
            tree.preorder(),
            [60, 30, 20, 40, 70, 80]
        )

    def test_BST_13(self):
        tree = BST()
        tree.insert(50)
        tree.insert(30)
        self.assertTrue(tree.delete(50))
        self.assertEqual(tree.root.key, 30)
        self.assertTrue(tree.delete(30))
        self.assertIsNone(tree.root)
        self.assertTrue(tree.is_empty())
        tree.insert(100)
        self.assertEqual(tree.root.key, 100)
        self.assertEqual(len(tree), 1)

    def test_BST_14(self):
        tree = self.create_reference_tree()
        original = tree.inorder()
        self.assertFalse(tree.delete(999))
        self.assertEqual(tree.inorder(), original)
        empty = BST()
        self.assertFalse(empty.delete(999))
        self.assertEqual(len(empty), 0)
        self.assertIsNone(empty.root)

    def test_BST_15(self):
        tree = BST()
        for key in [50, 30, 70, 60, 65]:
            tree.insert(key)

        self.assertTrue(tree.delete(50))
        self.assertEqual(
            tree.preorder(),
            [60, 30, 70, 65]
        )

        self.assertEqual(
            tree.inorder(),
            [30, 60, 65, 70]
        )

        self.assertTrue(tree.is_valid_bst())

    def test_BST_16(self):
        keys = [50, 30, 70, 20, 40, 60, 80]
        for deletion_order in [keys, list(reversed(keys))]:
            tree = self.create_reference_tree()
            remaining = set(keys)

            for key in deletion_order:
                with self.subTest(order=deletion_order, key=key):
                    self.assertTrue(tree.delete(key))

                    remaining.remove(key)
                    self.assertTrue(tree.is_valid_bst())
                    self.assertEqual(len(tree), len(remaining))
                    
                    self.assertEqual(
                        tree.inorder(),
                        sorted(remaining)
                    )

    def test_BST_17(self):
        tree = self.create_reference_tree()
        self.assertEqual(
            tree.range_query(35, 65),
            [40, 50, 60]
        )

        self.assertEqual(
            tree.range_query(30, 70),
            [30, 40, 50, 60, 70]
        )

        self.assertEqual(
            tree.range_query(0, 100),
            [20, 30, 40, 50, 60, 70, 80]
        )

        self.assertEqual(tree.range_query(51, 59), [])
        self.assertEqual(tree.range_query(70, 30), [])
        empty = BST()
        self.assertEqual(empty.range_query(0, 100), [])

    def test_BST_18(self):
        tree = BST()
        for key in ["dog", "cat", "emu", "ant"]:
            tree.insert(key)

        self.assertEqual(
            tree.inorder(),
            ["ant", "cat", "dog", "emu"]
        )

        self.assertEqual(tree.min_key(), "ant")
        self.assertEqual(tree.max_key(), "emu")

    def test_BST_19(self):
        tree = self.create_reference_tree()
        self.assertTrue(tree.is_valid_bst())
        tree.root.left.right.key = 55
        self.assertFalse(tree.is_valid_bst())

    def test_BST_20(self):
        random.seed(93)
        tree = BST()
        model = []
        for _ in range(1000):
            key = random.randint(0, 200)
            operation = random.choice(["insert", "delete"])
            if operation == "insert":
                tree.insert(key)

                if key not in model:
                    model.append(key)
                    model.sort()

            else:
                result = tree.delete(key)
                if key in model:
                    model.remove(key)
                    self.assertTrue(result)
                else:
                    self.assertFalse(result)

            self.assertEqual(tree.inorder(), model)
            self.assertEqual(len(tree), len(model))
            self.assertTrue(tree.is_valid_bst())

    def test_BST_21(self):
        tree = BST()

        for key in [1, 2, 3, 4]:
            tree.insert(key)

        self.assertEqual(
            tree.level_order(),
            [1, 2, 3, 4]
        )

        tree2 = BST()

        for key in [5, 3]:
            tree2.insert(key)

        self.assertEqual(
            tree2.level_order(),
            [5, 3]
        )

if __name__ == "__main__":
    unittest.main()