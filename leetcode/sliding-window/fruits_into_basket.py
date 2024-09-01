from collections import defaultdict
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = defaultdict(int)
        res = l = 0
        for r in range(len(fruits)):
            window[fruits[r]] += 1

            while len(window) > 2:
                toRemove = fruits[l]
                window[toRemove] -= 1
                l += 1

                if not window[toRemove]:
                    window.pop(toRemove)

            res = max(res, (r - l) + 1)
        return res
