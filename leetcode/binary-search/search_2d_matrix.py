from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            l, r = 0, len(m) - 1
            
            if m[l] <= target and m[r] >= target:
                while l <= r:
                    mid = l + ((r - l) // 2)

                    if m[mid] > target:
                        r = mid - 1
                    elif m[mid] < target:
                        l = mid + 1
                    else:
                        return True
        return False