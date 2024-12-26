from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        foundNull = False

        while q:
            qLen = len(q)

            for _ in range(qLen):
                cur = q.popleft()

                if cur and foundNull:
                    return False
                elif cur:
                    q.append(cur.left)
                    q.append(cur.right)
                else:
                    foundNull = True

        return True
