from heapq import heappush, heappop
from typing import List
from collections import defaultdict


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        maxHeap = [(-1, start)]
        visited = set()

        adj = defaultdict(list)
        for (u, v), sp in zip(edges, succProb):
            adj[u].append([v, sp])
            adj[v].append([u, sp])

        while maxHeap:
            prob, cur = heappop(maxHeap)
            visited.add(cur)

            if cur == end:
                return prob * -1

            for neigh, edgeProb in adj[cur]:
                if neigh not in visited:
                    heappush(maxHeap, (prob * edgeProb, neigh))

        return 0
