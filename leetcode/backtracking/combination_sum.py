from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i: int, cur: List[int], cur_sum: int) -> None:
            if cur_sum == target:
                res.append(cur.copy())
                return

            if i == len(nums) or cur_sum > target:
                return

            cur.append(nums[i])
            backtrack(i, cur, cur_sum + nums[i])

            cur.pop()
            backtrack(i + 1, cur, cur_sum)

        backtrack(0, [], 0)
        return res
