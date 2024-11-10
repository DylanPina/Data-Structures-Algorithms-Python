from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubstring(removed: set[int]) -> int:
            s_i = p_i = 0
            while s_i < len(s) and p_i < len(p):
                if s_i not in removed and s[s_i] == p[p_i]:
                    p_i += 1
                s_i += 1
            return p_i == len(p)

        res = 0
        l, r = 0, len(removable) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            if isSubstring(set(removable[: m + 1])):
                res = max(res, m + 1)
                l = m + 1
            else:
                r = m - 1
        return res
