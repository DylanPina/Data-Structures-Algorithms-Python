from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]):
        if not root:
            return True

        queue = deque([root])
        even = True

        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()

                if even and (node.val % 2 == 0 or prev and node.val <= prev):
                    return False
                if not even and (node.val % 2 == 1 or prev and node.val >= prev):
                    return False

                prev = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            even = not even

        return True
