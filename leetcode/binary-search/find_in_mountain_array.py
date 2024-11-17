# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, arr: "MountainArray") -> int:
        # Binary search to find inflection point
        l, r = 1, arr.length() - 2
        inflectionIndex = arr.length()
        while l <= r:
            m = l + ((r - l) // 2)
            left, mid, right = arr.get(m - 1), arr.get(m), arr.get(m + 1)
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                inflectionIndex = m
                break

        def binarySearch(l: int, r: int, incline: bool) -> int:
            while l <= r:
                m = l + ((r - l) // 2)
                val = arr.get(m)
                if val > target:
                    if incline:
                        r = m - 1
                    else:
                        l = m + 1
                elif val < target:
                    if incline:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    return m
            return -1

        # Search incline
        l, r = 0, inflectionIndex
        foundTargetIncline = binarySearch(l, r, True)
        if foundTargetIncline != -1:
            return foundTargetIncline

        # Search decline
        l, r = inflectionIndex, arr.length() - 1
        foundTargetDecline = binarySearch(l, r, False)
        if foundTargetDecline != -1:
            return foundTargetDecline

        return -1
