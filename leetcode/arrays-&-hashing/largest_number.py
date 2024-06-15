from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = []
        for num in nums:
            res.append(str(num))

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            return 1

        nums = sorted(res, key=cmp_to_key(compare))
        return str(int("".join(res)))
