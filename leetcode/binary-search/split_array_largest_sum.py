from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l, r = max(nums), sum(nums)
        res = r

        def canSplit(largest):
            subarrays = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subarrays += 1
                    curSum = n
            return subarrays + 1 <= k

        while l <= r:
            mid = l + ((r - l) // 2)
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
