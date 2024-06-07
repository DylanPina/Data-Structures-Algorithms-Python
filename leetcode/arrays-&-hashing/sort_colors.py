from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1

        i = 0
        for num, freq in enumerate(counts):
            for _ in range(freq):
                nums[i] = num
                i += 1
