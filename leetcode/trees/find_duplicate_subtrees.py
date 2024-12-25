from collections import defaultdict
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        subtrees = defaultdict(list)
        res = []

        def dfs(node: Optional[TreeNode]):
            if not node:
                return "None"

            s = ",".join([str(node.val), dfs(node.left), dfs(node.right)])
            if len(subtrees[s]) == 1:
                res.append(node)
            subtrees[s].append(node)
            return s

        dfs(root)
        return res
