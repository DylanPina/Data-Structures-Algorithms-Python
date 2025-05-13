import math
from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        INF = math.inf

        dist = [[INF] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = dist[v][u] = min(dist[u][v], w)

        for k in range(n):
            d_k = dist[k]
            for i in range(n):
                d_i, d_ik = dist[i], dist[i][k]
                if d_ik == INF:
                    continue

                for j in range(n):
                    if (val := d_ik + d_k[j]) < d_i[j]:
                        d_i[j] = val

        # pick city with fewest reachable ≤ threshold
        def reachable_count(i: int):
            return sum(1 for d in dist[i] if d <= distanceThreshold)

        # tie-break by larger index ⇒ iterate in natural order
        return min(range(n), key=lambda i: (reachable_count(i), -i))
