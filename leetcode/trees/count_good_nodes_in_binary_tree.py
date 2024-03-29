class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(root, maxVal) -> None:
            if not root:
                return
            
            maxVal = max(maxVal, root.val)
            if root.val >= maxVal:
                self.count += 1

            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

        dfs(root, root.val)
        return self.count