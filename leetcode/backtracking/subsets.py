from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i: int, cur: List[int]) -> None:
            if i == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            backtrack(i + 1, cur)

            cur.pop()
            backtrack(i + 1, cur)

        backtrack(0, [])
        return res
