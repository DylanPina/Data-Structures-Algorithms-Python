from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)

        adj = {i: [] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)

        res = 0
        visit, path = set(), set()
        count = [[0] * 26 for i in range(n)]

        # Return max req of color
        def dfs(node: int) -> int:
            if node in path:
                return float("inf")
            if node in visit:
                return 0

            visit.add(node)
            path.add(node)

            color_i = ord(colors[node]) - ord("a")
            count[node][color_i] = 1

            for nei in adj[node]:
                if dfs(nei) == float("inf"):
                    return float("inf")

                for c in range(26):
                    count[node][c] = max(
                        count[node][c], count[nei][c] + (1 if c == color_i else 0)
                    )

            path.remove(node)
            return max(count[node])

        for node in range(n):
            if dfs(node) == float("inf"):
                return -1

            res = max(res, max(count[node]))

        return res
