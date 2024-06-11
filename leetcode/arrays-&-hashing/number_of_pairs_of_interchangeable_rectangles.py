from collections import defaultdict
from typing import List
from math import factorial


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_map = defaultdict(int)
        for width, height in rectangles:
            ratio = width / height
            ratio_map[ratio] += 1

        res = 0
        for ratio, occurences in ratio_map.items():
            if occurences <= 1:
                continue
            res += factorial(occurences) / (2 * factorial(occurences - 2))
        return int(res)
