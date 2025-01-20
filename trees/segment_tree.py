class SegmentTree:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

    # O(n)
    @staticmethod
    def build(nums, L, R):
        if L == R:
            return SegmentTree(nums[L], L, R)

        M = (L + R) // 2
        root = SegmentTree(0, L, R)
        root.left = SegmentTree.build(nums, L, M)
        root.right = SegmentTree.build(nums, M + 1, R)
        root.sum = root.left.sum + root.right.sum
        return root

    # O(logn)
    def update(self, index, val) -> None:
        if self.L == self.R:
            self.sum = val
            return

        M = (self.L + self.R) // 2
        if index > M and self.right:
            self.right.update(index, val)
        elif self.left:
            self.left.update(index, val)
        self.sum = (self.left.sum if self.left else 0) + (
            self.right.sum if self.right else 0
        )

    # O(logn)
    def rangeQuery(self, L, R) -> int:
        if L == self.L and R == self.R:
            return self.sum

        M = (self.L + self.R) // 2
        if L > M and self.right:
            return self.right.rangeQuery(L, R)
        elif R <= M and self.left:
            return self.left.rangeQuery(L, R)
        elif self.left and self.right:
            return self.left.rangeQuery(L, M) + self.right.rangeQuery(M + 1, R)
        else:
            return self.left.sum if self.left else self.right.sum if self.right else 0
