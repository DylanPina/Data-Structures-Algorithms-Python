from collections import defaultdict
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        occurences = defaultdict(int)
        for num in nums:
            occurences[num] += 1

        res = [[] for _ in range(max(occurences.values()))]
        for num, occurence in occurences.items():
            for i in range(occurence):
                res[i].append(num)
        return res
