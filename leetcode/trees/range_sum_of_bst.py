from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0

        def inRange(value: int):
            return low <= value and value <= high

        def dfs(node: Optional[TreeNode]):
            nonlocal res
            if not node:
                return

            res += node.val if inRange(node.val) else 0
            if node.val <= high:
                dfs(node.right)
            if node.val >= low:
                dfs(node.left)

        dfs(root)
        return res
