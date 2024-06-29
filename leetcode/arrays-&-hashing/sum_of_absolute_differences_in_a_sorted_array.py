from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        totalSum = sum(nums)
        res, prefix = [], 0

        for i, n in enumerate(nums):
            postfix = totalSum - n - prefix
            leftSize, rightSize = i, len(nums) - i - 1

            res.append(leftSize * n - prefix + postfix - rightSize * n)
            prefix += n
        return res
