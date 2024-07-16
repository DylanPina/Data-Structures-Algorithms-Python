from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        numsRange = [i for i in range(1, len(nums) + 1)]

        for num in numsRange:
            if num not in numsSet:
                return num
        return len(nums) + 1
