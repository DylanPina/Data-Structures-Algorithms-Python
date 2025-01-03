from heapq import heapify, heappop, heappush
from typing import Counter, List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = [(count, num) for num, count in Counter(arr).items()]
        heapify(freq)
        for _ in range(k):
            count, num = heappop(freq)
            if count > 1:
                heappush(freq, (count - 1, num))
        return len(freq)
