from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node: Optional[TreeNode], curSum: int) -> bool:
            if not node:
                return False

            curSum += node.val
            if not node.left and not node.right:
                return curSum == targetSum
            return dfs(node.left, curSum) or dfs(node.right, curSum)

        return dfs(root, 0)
