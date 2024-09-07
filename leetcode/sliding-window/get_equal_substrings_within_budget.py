class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = l = diff = 0
        for r in range(len(s)):
            diff += abs(ord(s[r]) - ord(t[r]))
            while diff > maxCost and l <= r:
                diff -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            res = max(res, (r - l) + 1)
        return res
