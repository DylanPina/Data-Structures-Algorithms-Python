from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, combination = [], []

        def helper(i: int, cur_sum: int) -> None:
            if cur_sum == target:
                res.append(combination.copy())
                return

            if i == len(candidates) or cur_sum > target:
                return

            combination.append(candidates[i])
            helper(i, cur_sum + candidates[i])

            combination.pop()
            helper(i + 1, cur_sum)

        helper(0, 0)
        return res
