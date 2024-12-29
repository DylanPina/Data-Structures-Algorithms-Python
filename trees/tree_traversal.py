from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFS:

    # Preorder traversal (Non-Recursive)
    @staticmethod
    def preorder(root: Optional[TreeNode]) -> None:
        if not root:
            return

        stack = [root]
        while stack:
            node = stack.pop()
            print(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    # Preorder traversal (Recursive)
    @staticmethod
    def preorder_recursive(root: Optional[TreeNode]) -> None:
        if not root:
            return

        print(root.val)
        DFS.preorder_recursive(root.left)
        DFS.preorder_recursive(root.right)

    # Inorder traversal (Non-Recursive)
    @staticmethod
    def inorder(root: Optional[TreeNode]) -> None:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            print(root.val if root else "")
            root = root.right if root else None

    # Inorder traversal (Recursive)
    @staticmethod
    def inorder_recursive(root: Optional[TreeNode]) -> None:
        if not root:
            return

        DFS.inorder_recursive(root.left)
        print(root.val)
        DFS.inorder_recursive(root.right)

    # Postorder traversal (Non-Recursive)
    @staticmethod
    def postorder(root):
        stack = [(root, False)]  # Node, Visited
        while stack:
            curr, visited = stack.pop()
            if curr:
                if visited:
                    print(curr.val)
                else:
                    stack.append((curr, True))
                    stack.append((curr.right, False))
                    stack.append((curr.left, False))

    # Postorder traversal (Recursive)
    @staticmethod
    def postorder_recursive(root: Optional[TreeNode]) -> None:
        if not root:
            return

        DFS.postorder_recursive(root.left)
        DFS.postorder_recursive(root.right)
        print(root.val)


class BFS:
    # Level-order traversal (Non-Recursive)
    @staticmethod
    def level_order(root: Optional[TreeNode]) -> None:
        if not root:
            return

        queue = deque([root])
        while queue:
            node = queue.popleft()
            print(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # Level-order traversal (Recursive)
    @staticmethod
    def level_order_recursive(root: Optional[TreeNode]) -> None:
        if not root:
            return

        # Helper function to traverse a specific level
        def traverse_level(node: Optional[TreeNode], level: int) -> None:
            if not node:
                return

            if level == 0:
                print(node.val)
            else:
                traverse_level(node.left, level - 1)
                traverse_level(node.right, level - 1)

        # Determine the depth of the tree
        def tree_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + max(tree_depth(node.left), tree_depth(node.right))

        depth = tree_depth(root)
        for i in range(depth):
            traverse_level(root, i)
