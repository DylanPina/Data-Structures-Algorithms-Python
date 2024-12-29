from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], path_mask: int) -> int:
            if not node:
                return 0

            path_mask ^= 1 << node.val

            # If it's a leaf node
            if not node.left and not node.right:
                # Check if at most one bit is set in the path_mask
                return int(path_mask & (path_mask - 1) == 0)

            # Continue the DFS traversal
            return dfs(node.left, path_mask) + dfs(node.right, path_mask)

        return dfs(root, 0)
