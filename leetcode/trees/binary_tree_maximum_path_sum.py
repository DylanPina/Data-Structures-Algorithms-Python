from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        res = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            res = max(res, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return int(res)
