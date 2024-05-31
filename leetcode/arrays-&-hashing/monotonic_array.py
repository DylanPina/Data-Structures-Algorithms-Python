from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing, decreasing = False, False
        
        for i in range(len(nums) - 1):
            num1, num2 = nums[i], nums[i + 1]
            
            if num1 < num2:
                if decreasing:
                    return False
                increasing = True

            if num1 > num2:
                if increasing:
                    return False
                decreasing = True
        
        return True
