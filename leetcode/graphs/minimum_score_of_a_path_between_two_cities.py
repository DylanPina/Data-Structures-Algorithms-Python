from collections import defaultdict
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, distance in roads:
            adj[u].append((v, distance))
            adj[v].append((u, distance))

        res = float("inf")
        visited = set()

        def dfs(node: int) -> None:
            nonlocal res

            if node in visited:
                return

            visited.add(node)

            for nei, dist in adj[node]:
                res = min(res, dist)
                dfs(nei)

        dfs(1)
        return int(res)
