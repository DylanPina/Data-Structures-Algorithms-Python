from typing import Counter, List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        perms, cur_perm = [], []

        def dfs() -> None:
            if len(cur_perm) == len(nums):
                perms.append(cur_perm.copy())
                return

            for num in count:
                if count[num] == 0:
                    continue

                cur_perm.append(num)
                count[num] -= 1

                dfs()

                cur_perm.remove(num)
                count[num] += 1

        dfs()
        return perms
