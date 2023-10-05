from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            self.prefix.append(sum)

    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.prefix[left - 1] if left > 0 else 0
        right_sum = self.prefix[right]
        return right_sum - left_sum