from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert_level_order(self, data): # Inserção automática por nível, partindo da raiz
        root = self.root
        if root is None:
            root = Node(data)
            return root

        q = deque()
        q.append(root)

        while q:

            curr = q.popleft()

            if curr.left is not None:
                q.append(curr.left)
            else:
                curr.left = Node(data)
                return root

            if curr.right is not None:
                q.append(curr.right)
            else:
                curr.right = Node(data)
                return root

    def inorder(self, node: Node):
        current = node
        if current is None:
            return

        self.inorder(current.left)
        print(current.data)
        self.inorder(current.right)


    def preorder(self, node: Node):
        current = node
        if current is None:
            return

        print(current.data)
        self.preorder(current.left)
        self.preorder(current.right)

    def postorder(self, node: Node):
        current = node
        if current is None:
            return

        self.postorder(current.left)
        self.postorder(current.right)
        print(current.data)

    def level_order(self):
        root = self.root

        if root is None:
            return []

        q = []
        res = []

        q.append(root)
        curr_level = 0

        while q:
            len_q = len(q)
            res.append([])

            for _ in range(len_q):
                node = q.pop(0)
                res[curr_level].append(node.data)

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)
            curr_level += 1
        return res

    def is_perfect(self, node: Node, profundidade=None, nivel=0):
        if not node:
            return False

        if not node.left and not node.right:
            return True

        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        b_factor = abs(left_height - right_height)

        return (b_factor == 0) and self.is_regular(node)

    def is_complete(self, node: Node):
        return self.is_balanced(node) and self.is_regular(node)

    def is_regular(self, node: Node):
        if not node:
            return False

        zero_or_two_children = (node.left is None) == (node.right is None)
        if node.right:
            zero_or_two_children = zero_or_two_children and self.is_regular(node.right)
        if node.left:
            zero_or_two_children = zero_or_two_children and self.is_regular(node.left)

        return zero_or_two_children

    def is_balanced(self, node: Node):
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        b_factor = abs(left_height - right_height)

        return b_factor < 2

    def is_unbalanced(self, node: Node):
        return not self.is_balanced(node)

    def count_nodes(self, node: Node):
        if not node:
            return 0
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def get_height(self, node: Node):
        if not node:
            return -1

        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        return 1 + max(left_height, right_height)

if __name__ == "__main__":
    tree = BinaryTree()

    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.right.left = Node("D")
    tree.root.right.right = Node("E")

    print(tree.is_complete(tree.root))
