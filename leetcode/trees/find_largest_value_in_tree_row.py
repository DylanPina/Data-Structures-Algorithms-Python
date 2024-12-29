from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque([root])
        while q:
            qLen = len(q)
            maxVal = float("-inf")

            for _ in range(qLen):
                cur = q.popleft()
                maxVal = max(maxVal, cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            res.append(maxVal)
        return res
