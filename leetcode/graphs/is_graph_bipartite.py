from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0] * len(graph)  # Map node i -> odd=1, even=-1

        def dfs(i: int, c: int):
            color[i] = c
            for nei in graph[i]:
                if color[nei] == c:
                    return False
                if color[nei] == 0 and not dfs(nei, -c):
                    return False
            return True

        for i in range(len(graph)):
            if color[i] == 0 and not dfs(i, 1):
                return False
        return True
