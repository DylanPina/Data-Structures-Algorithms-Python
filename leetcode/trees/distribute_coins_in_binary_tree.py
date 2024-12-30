from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res
            if not node:
                return 0

            leftCoins = dfs(node.left)
            rightCoins = dfs(node.right)

            balance = node.val + leftCoins + rightCoins - 1
            res += abs(balance)

            return balance

        dfs(root)
        return res
