from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        s_count, p_count = defaultdict(int), defaultdict(int)
        for i in range(len(p)):
            p_i, s_i = p[i], s[i]
            p_count[p_i] += 1
            s_count[s_i] += 1

        res = [0] if s_count == p_count else []
        l = 0
        for r in range(len(p), len(s)):
            s_count[s[r]] += 1
            s_count[s[l]] -= 1

            if not s_count[s[l]]:
                s_count.pop(s[l])

            l += 1
            if s_count == p_count:
                res.append(l)
        return res
