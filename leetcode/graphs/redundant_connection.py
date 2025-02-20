from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i: i for i in range(len(edges) + 1)}
        rank = {i: 0 for i in range(len(edges) + 1)}

        for node in parent.keys():
            rank[node] = 1

        def find(x: int) -> int:
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: int, y: int) -> bool:
            if (x := find(x)) == (y := find(y)):
                return False

            if rank[x] > rank[y]:
                parent[y] = x
            elif rank[y] > rank[x]:
                parent[x] = y
            else:
                parent[y] = x
                rank[x] += 1

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []
