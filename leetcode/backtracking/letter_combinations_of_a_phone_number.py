from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        digits_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i: int, cur: List[str]) -> None:
            if i == len(digits):
                res.append("".join(cur))
                return

            for c in digits_map[digits[i]]:
                cur.append(c)
                backtrack(i + 1, cur)
                cur.pop()

        backtrack(0, [])
        return res
