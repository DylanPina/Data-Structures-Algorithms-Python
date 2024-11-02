from typing import List


class Solution:
    def search(self, n: List[int], t: int) -> bool:
        l, r = 0, len(n) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if n[m] == t:
                return True

            if n[l] == n[m]:
                l += 1
            # Left sorted partition
            elif n[l] < n[m]:
                if n[l] <= t < n[m]:
                    r = m - 1
                else:
                    l = m + 1
            # Right sorted partition
            else:
                if n[m] < t <= n[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False
