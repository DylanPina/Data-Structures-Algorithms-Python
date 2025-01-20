from collections import defaultdict
from typing import Dict, List
from heapq import heappush, heappop


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))

        shortest = {}
        minHeap = [[0, src]]
        while minHeap:
            for _ in range(len(minHeap)):
                w1, n1 = heappop(minHeap)
                if n1 in shortest:
                    continue
                shortest[n1] = w1

                for n2, w2 in adj[n1]:
                    if n2 not in shortest:
                        heappush(minHeap, [w1 + w2, n2])

        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest
