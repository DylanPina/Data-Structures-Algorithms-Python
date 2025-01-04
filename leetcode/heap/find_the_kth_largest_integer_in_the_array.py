from typing import List
from heapq import nlargest


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return nlargest(k, nums, key=lambda n: int(n))[-1]
