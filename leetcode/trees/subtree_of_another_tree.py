from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        elif not root:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, n1: Optional[TreeNode], n2: Optional[TreeNode]) -> bool:
        if not n1 and not n2:
            return True
        if (not n1 or not n2) or (n1.val != n2.val):
            return False
        return self.isSameTree(n1.left, n2.left) and self.isSameTree(n1.right, n2.right)
