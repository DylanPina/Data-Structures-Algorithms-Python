from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, combination = [], []

        def helper(i: int) -> None:
            if len(combination) == k:
                res.append(combination.copy())
                return

            if i > n:
                return

            for j in range(i, n + 1):
                combination.append(j)
                helper(j + 1)
                combination.pop()

        helper(1)
        return res
