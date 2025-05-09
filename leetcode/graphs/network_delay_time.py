import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        res = 0
        pq = [(0, k)]  # time, vertex
        visited = set()

        while pq:
            for _ in range(len(pq)):
                t1, u = heapq.heappop(pq)
                if u in visited:
                    continue

                res = t1

                visited.add(u)
                if len(visited) == n:
                    return res

                for v, t2 in adj[u]:
                    if v not in visited:
                        heapq.heappush(pq, (t1 + t2, v))

        return -1
