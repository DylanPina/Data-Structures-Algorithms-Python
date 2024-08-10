from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        s_i = g_i = 0
        while s_i < len(s) and g_i < len(g):
            if g[g_i] <= s[s_i]:
                g_i += 1
            s_i += 1
        return g_i
