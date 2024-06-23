class Solution:
    def partitionString(self, s: str) -> int:
        cur, res = set(), 0
        for c in s:
            if c in cur:
                res += 1
                cur.clear()
            cur.add(c)
        return res + 1
