from heapq import heappop, heappush
from typing import List


class Solution:
    def fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        flowers = sorted(flowers)
        peoplePairs = sorted([(p, i) for i, p in enumerate(people)])
        blooming = []
        res = [0] * len(people)

        for p, i in peoplePairs:
            while flowers and flowers[0][0] <= p:
                heappush(blooming, heappop(flowers)[1])

            while blooming and blooming[0] < p:
                heappop(blooming)

            res[i] = len(blooming)

        return res
