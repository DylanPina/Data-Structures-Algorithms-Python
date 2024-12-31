from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        prev = 0

        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            nonlocal prev
            if not node:
                return None

            dfs(node.right)
            node.val += prev
            prev = node.val
            dfs(node.left)
            return node

        return dfs(root)
