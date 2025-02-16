from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {i: i for i in range(n)}
        rank = {i: 0 for i in range(n)}
        components = n

        def getParent(node: int) -> int:
            while not parent[node] == node:
                return getParent(parent[parent[node]])
            return node

        def union(x: int, y: int) -> bool:
            nonlocal components
            if (x := getParent(x)) == (y := getParent(y)):
                return False

            if rank[x] > rank[y]:
                parent[y] = parent[x]
            elif rank[y] > rank[x]:
                parent[x] = parent[y]
            else:
                parent[y] = parent[x]
                rank[x] += 1

            components -= 1
            return True

        for u, v in edges:
            union(u, v)

        return components
