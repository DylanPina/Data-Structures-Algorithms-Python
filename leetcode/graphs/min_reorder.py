from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(u, v) for u, v in connections}
        neighbors = {i: [] for i in range(n)}

        for u, v in connections:
            neighbors[u].append(v)
            neighbors[v].append(u)

        reorder = 0
        visited = set()

        def dfs(city: int) -> None:
            nonlocal reorder

            visited.add(city)

            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                if (neighbor, city) not in edges:
                    reorder += 1
                dfs(neighbor)

        dfs(0)
        return reorder
