import heapq
from collections import defaultdict
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj = defaultdict(list)
        for (n1, n2), p in zip(edges, succProb):
            adj[n1].append((n2, p))
            adj[n2].append((n1, p))

        pq = [(-1, start_node)]
        visit = set()

        while pq:
            for _ in range(len(pq)):
                p1, n1 = heapq.heappop(pq)

                if n1 == end_node:
                    return -p1

                visit.add(n1)

                for n2, p2 in adj[n1]:
                    if n2 not in visit:
                        heapq.heappush(pq, (p1 * p2, n2))
        return 0.0
