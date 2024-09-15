from collections import defaultdict
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        res, resLen = "", float("inf")
        windowCount, tCount = defaultdict(int), Counter(t)
        diff = len(tCount.keys())
        l = 0

        for r in range(len(s)):
            windowCount[s[r]] += 1

            if s[r] in tCount:
                if windowCount[s[r]] == tCount[s[r]]:
                    diff -= 1

            if not diff and resLen > (r - l + 1):
                res = s[l : r + 1]
                resLen = len(res)

            while not diff:
                if resLen > (r - l + 1):
                    res = s[l : r + 1]
                    resLen = len(res)

                if s[l] in tCount and windowCount[s[l]] == tCount[s[l]]:
                    diff += 1

                windowCount[s[l]] -= 1
                l += 1
        return res
