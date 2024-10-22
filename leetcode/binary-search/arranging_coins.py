class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = l + ((r - l) // 2)
            if mid * (mid + 1) // 2 > n:
                r = mid - 1
            else:
                l = mid + 1
        return r
