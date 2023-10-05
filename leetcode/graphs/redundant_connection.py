from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionFind = UnionFind(edges)

        for x, y in edges:
            if not unionFind.union(x, y):
                return [x, y]
        return [-1, -1]


class UnionFind:
    def __init__(self, edges):
        self.edges = edges
        self.parent = {i: i for i in range(1, len(edges) + 1)}
        self.rank = {i: 1 for i in range(1, len(edges) + 1)}

    def find(self, x: int) -> int:
        # Finds the root of x
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) -> bool:
        x_root, y_root = self.find(x), self.find(y)

        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
                self.rank[y_root] += self.rank[x_root]
            else:
                self.parent[y_root] = x_root
                self.rank[x_root] += self.rank[y_root]
            return True
        return False
