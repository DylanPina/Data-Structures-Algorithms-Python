import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        adj = defaultdict(list)
        for u, v, c in zip(original, changed, cost):
            adj[u].append((v, c))

        memo = {}

        def dijkstra(src: str) -> dict:
            if src in memo:
                return memo[src]

            min_cost_map = {}
            pq = [(0, src)]

            while pq:
                c_u, u = heapq.heappop(pq)

                if u in min_cost_map:
                    continue

                min_cost_map[u] = c_u

                for v, c_v in adj[u]:
                    heapq.heappush(pq, (c_u + c_v, v))

            memo[src] = min_cost_map
            return min_cost_map

        res = 0
        for u, v in zip(source, target):
            if v not in (min_cost_map := dijkstra(u)):
                return -1
            res += min_cost_map[v]

        return res
