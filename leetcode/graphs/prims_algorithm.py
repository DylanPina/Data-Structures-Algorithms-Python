from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, v))

        minHeap = [(0, 0)]
        res = 0
        visit = set()
        while minHeap and len(visit) < n:
            w, v = heappop(minHeap)
            if v in visit:
                continue

            res += w
            visit.add(v)
            for u, w in adj[v]:
                heappush(minHeap, (w, u))

        return res if len(visit) == n else -1
