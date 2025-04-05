from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: set() for i in range(n)}
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        visited = set()

        def dfs(u: int, component: set) -> set:
            visited.add(u)
            component.add(u)

            for v in adj[u]:
                if v not in visited and u != v:
                    dfs(v, component)

            return component

        complete_components = 0

        for i in range(n):
            if i in visited:
                continue

            component = dfs(i, set())
            if all([len(component) - 1 == len(adj[u]) for u in component]):
                complete_components += 1

        return complete_components
