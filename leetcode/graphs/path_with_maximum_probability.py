from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int,
    ) -> float:
        adj = defaultdict(list)
        for [u, v], w in zip(edges, succProb):
            adj[u].append((v, w))
            adj[v].append((u, w))

        shortest = {}
        maxHeap = [(1, start)]

        while maxHeap:
            for _ in range(len(maxHeap)):
                w1, n1 = heappop(maxHeap)

                if n1 in shortest:
                    continue
                if n1 == end:
                    return abs(w1)

                shortest[n1] = w1
                for n2, w2 in adj[n1]:
                    if not n2 in shortest:
                        heappush(maxHeap, (-abs(w1 * w2), n2))
        return 0.0
