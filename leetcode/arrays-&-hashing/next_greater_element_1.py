from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_map = {n: i for i, n in enumerate(nums1)}
        res, stack = [-1 for _ in nums1], []

        for num in nums2:
            while stack and num > stack[-1]:
                top = stack.pop()
                if top in nums1:
                    res[index_map[top]] = num
            stack.append(num)
        return res
