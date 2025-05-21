from collections import defaultdict
from typing import List


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        res = 0

        def dfs(u: int, par: int) -> None:
            nonlocal res

            total = values[u]

            for v in adj[u]:
                if not v == par:
                    total += dfs(v, u)

            if not total % k:
                res += 1

            return total

        dfs(0, -1)
        return res
