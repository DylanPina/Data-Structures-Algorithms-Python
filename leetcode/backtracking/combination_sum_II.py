from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i: int, cur: List[int], cur_sum: int) -> None:
            if cur_sum == target:
                res.append(cur.copy())
                return

            if i >= len(candidates) or cur_sum > target:
                return

            cur.append(candidates[i])
            backtrack(i + 1, cur, cur_sum + candidates[i])

            cur.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, cur, cur_sum)

        backtrack(0, [], 0)
        return res
