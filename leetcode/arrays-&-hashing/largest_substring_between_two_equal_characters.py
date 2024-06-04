class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res, map = -1, {}
        for i, c in enumerate(s):
            if c in map:
                res = max(res, i - map[c] - 1)
            else:
                map[c] = i
        return res
