class TreeNode:
    """Supports lookup and ordered traversals of the station directory"""
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BST:
    """Binary search tree stores key-value pairs in ordered nodes"""
    def __init__(self):
        self.root = None
        self.size = 0
        self.key_type = None

    def insert(self, key, value=None):
        if self.key_type is None:
            if type(key) != int and type(key) != str:
                raise TypeError("Key must be an integer or string")
            self.key_type = type(key)

        elif type(key) != self.key_type:
            raise TypeError("Cannot mix key types")

        if self.root is None:
            self.root = TreeNode(key, value)
            self.size += 1
            return

        current = self.root
        while True:
            if key == current.key:
                current.value = value
                return

            elif key < current.key:
                if current.left is None:
                    current.left = TreeNode(key, value)
                    self.size += 1
                    return
                current = current.left

            else:
                if current.right is None:
                    current.right = TreeNode(key, value)
                    self.size += 1
                    return
                current = current.right
    
    def contains(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return False

    def get(self, key):
        current = self.root
        while current != None:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        raise KeyError(key)

    def delete(self, key):
        def remove(node, key):
            if node is None:
                return None, False

            if key < node.key:
                node.left, deleted = remove(node.left, key)

            elif key > node.key:
                node.right, deleted = remove(node.right, key)

            else:
                if node.left is None:
                    return node.right, True

                if node.right is None:
                    return node.left, True

                successor = node.right

                while successor.left is not None:
                    successor = successor.left

                node.key = successor.key
                node.value = successor.value
                node.right, deleted = remove(
                    node.right, successor.key
                )
                
                return node, True

            return node, deleted

        self.root, deleted = remove(self.root, key)

        if deleted:
            self.size -= 1

        return deleted

    def inorder(self):
        result = []
        def traverse(node):
            if node is not None:
                traverse(node.left)
                result.append(node.key)
                traverse(node.right)

        traverse(self.root)
        return result

    def preorder(self):
        result = []
        def traverse(node):
            if node is not None:
                result.append(node.key)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)
        return result

    def postorder(self):
        result = []
        def traverse(node):
            if node is not None:
                traverse(node.left)
                traverse(node.right)
                result.append(node.key)

        traverse(self.root)
        return result

    def level_order(self):
        if self.root is None:
            return []

        result = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.key)

            if node.left != None:
                queue.append(node.left)

            if node.right != None:
                queue.append(node.right)

        return result

    def height(self):
        def calculate(node):
            if node is None:
                return 0

            return 1 + max(calculate(node.left), calculate(node.right))
        
        return calculate(self.root)

    def min_key(self):
        if self.root is None:
            raise ValueError("Tree is empty")

        current = self.root
        while current.left is not None:
            current = current.left

        return current.key

    def max_key(self):
        if self.root is None:
            raise ValueError("Tree is empty")

        current = self.root
        while current.right is not None:
            current = current.right

        return current.key

    def count_leaves(self):
        def count(node):
            if node is None:
                return 0

            if node.left is None and node.right is None:
                return 1

            return count(node.left) + count(node.right)

        return count(self.root)

    def range_query(self, low, high):
        result = []
        if low > high:
            return result

        def search(node):
            if node is None:
                return

            if node.key > low:
                search(node.left)

            if low <= node.key <= high:
                result.append(node.key)

            if node.key < high:
                search(node.right)

        search(self.root)
        return result

    def is_valid_bst(self):
        def validate(node, lower, upper):
            if node is None:
                return True

            if lower is not None and node.key <= lower:
                return False

            if upper is not None and node.key >= upper:
                return False

            return (
                validate(node.left, lower, node.key)
                and validate(node.right, node.key, upper)
            )

        return validate(self.root, None, None)

    def is_empty(self):
        return self.root == None

    def __len__(self):
        return self.size