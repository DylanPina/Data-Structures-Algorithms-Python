from collections.abc import Generator
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.iter = self._inorder(root)
        self.nxt = next(self.iter, None)

    def _inorder(self, node: Optional[TreeNode]) -> Generator[int, None, None]:
        stack = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.val if node else -1
            node = node.right if node else None

    def next(self) -> int:
        res = self.nxt
        self.nxt = next(self.iter, None)
        return res or -1

    def hasNext(self) -> bool:
        return self.nxt is not None
