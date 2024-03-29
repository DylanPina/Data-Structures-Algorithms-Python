from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append([w, v])

        minheap = [[0, k]]  # [weight, src]
        time = 0
        visited = set()
        while minheap:
            w1, v1 = heapq.heappop(minheap)
            if v1 in visited:
                continue

            time = w1
            visited.add(v1)

            for w2, v2 in adj[v1]:
                if v2 not in visited:
                    heapq.heappush(minheap, [w1 + w2, v2])

        return time if len(visited) == n else -1
