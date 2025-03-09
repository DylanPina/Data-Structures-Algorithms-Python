from collections import defaultdict
from math import ceil
from typing import List


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj = defaultdict(list)
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)

        res = 0

        def dfs(node: int, parent: int) -> int:
            nonlocal res

            passengers = 0
            for child in adj[node]:
                if child == parent:
                    continue
                p = dfs(child, node)
                passengers += p
                res += int(ceil(p / seats))
            return passengers + 1

        dfs(0, -1)
        return res
