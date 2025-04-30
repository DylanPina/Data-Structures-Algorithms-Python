from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k:
            return False

        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)

        def backtrack(i: int, k: int, subset_sum: int) -> bool:
            if k == 0:
                return True
            if subset_sum == target:
                return backtrack(0, k - 1, 0)

            for j in range(i, len(nums)):
                if used[j] or subset_sum + nums[j] > target:
                    continue

                used[j] = True
                if backtrack(j + 1, k, subset_sum + nums[j]):
                    return True
                used[j] = False

            return False

        return backtrack(0, k, 0)
