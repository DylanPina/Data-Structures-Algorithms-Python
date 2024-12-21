from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return

            res.append(f"({str(node.val)}")

            if not node.left and node.right:
                res.append("()")
            else:
                dfs(node.left)

            dfs(node.right)
            res.append(f")")

        dfs(root)
        return "".join(res)[1:-1]
