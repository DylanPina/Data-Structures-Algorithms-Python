from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(
        self, r1: Optional[TreeNode], r2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not r1 and not r2:
            return None

        v1 = r1.val if r1 else 0
        v2 = r2.val if r2 else 0
        node = TreeNode(v1 + v2)
        node.left = self.mergeTrees(r1.left if r1 else None, r2.left if r2 else None)
        node.right = self.mergeTrees(r1.right if r1 else None, r2.right if r2 else None)
        return node
