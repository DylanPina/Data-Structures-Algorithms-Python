from collections import Counter
from heapq import heappop, heappush


class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""

        maxHeap = sorted([(-count, char) for char, count in Counter(s).items()])
        prev = None
        res = []

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            cnt, char = heappop(maxHeap)
            res.append(char)

            if prev:
                heappush(maxHeap, prev)
                prev = None
            if cnt + 1:
                prev = (cnt + 1, char)

        return "".join(res)
