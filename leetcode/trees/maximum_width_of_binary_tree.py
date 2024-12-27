from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([(root, 0)])
        maxWidth = 0

        while q:
            qLen = len(q)
            maxWidth = max(maxWidth, q[-1][1] - q[0][1] + 1)

            for _ in range(qLen):
                node, i = q.popleft()

                if node.left:
                    q.append((node.left, 2 * i))

                if node.right:
                    q.append((node.right, 2 * i + 1))

        return maxWidth
