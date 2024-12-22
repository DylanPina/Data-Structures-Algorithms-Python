from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        if not root:
            return None

        if (root.val >= p.val and root.val <= q.val) or (
            root.val <= p.val and root.val >= q.val
        ):
            return root

        return self.lowestCommonAncestor(root.left, p, q) or self.lowestCommonAncestor(
            root.right, p, q
        )
