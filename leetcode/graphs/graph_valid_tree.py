from typing import List
from collections import defaultdict


class Solution:

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = defaultdict(list)
        visited = set()

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        def dfs(cur: int, prev: int) -> bool:
            if cur in visited:
                return False

            visited.add(cur)
            for nei in visited:
                if nei == prev:
                    continue
                if not dfs(nei, cur):
                    return False
            return True

        return dfs(0, -1) and len(set) == n
