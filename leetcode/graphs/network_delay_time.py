from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        shortest = {}
        minHeap = [(0, k)]

        while minHeap:
            for _ in range(len(minHeap)):
                w1, n1 = heappop(minHeap)
                if n1 in shortest:
                    continue
                shortest[n1] = w1

                for n2, w2 in adj[n1]:
                    if n2 not in shortest:
                        heappush(minHeap, (w1 + w2, n2))

        return max(shortest.values()) if len(shortest) == n else -1
