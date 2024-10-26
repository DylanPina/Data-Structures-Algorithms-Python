from typing import List


class Solution:
    def findPeakElement(self, n: List[int]) -> int:
        l, r = 0, len(n) - 1
        m = 0

        while l <= r:
            m = l + ((r - l) // 2)
            if m < len(n) - 1 and n[m] < n[m + 1]:
                l = m + 1
            elif m > 0 and n[m] < n[m - 1]:
                r = m - 1
            else:
                break

        return m
