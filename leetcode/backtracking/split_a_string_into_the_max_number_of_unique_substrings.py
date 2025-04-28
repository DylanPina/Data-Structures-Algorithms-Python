class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(i: int, cur: set[int]) -> None:
            if i == len(s):
                return 0

            res = 0
            for j in range(i, len(s)):
                if (sub_str := s[i : j + 1]) not in cur:
                    cur.add(sub_str)
                    res = max(res, 1 + backtrack(j + 1, cur))
                    cur.remove(sub_str)
            return res

        return backtrack(0, set())
