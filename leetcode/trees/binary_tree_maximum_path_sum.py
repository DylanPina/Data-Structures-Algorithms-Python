class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPath = float("-inf")

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal maxPath
            if not root:
                return 0

            left, right = dfs(root.left), dfs(root.right)
            leftMax = max(left, 0)
            rightMax = max(right, 0)
            maxPath = max(maxPath, root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return maxPath
