from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            prefix.append(sum)
        
        for i in range(len(nums)):
            left = prefix[i - 1] if i > 0 else 0
            right = prefix[-1] - prefix[i]
            if right == left:
                return i
        return -1
