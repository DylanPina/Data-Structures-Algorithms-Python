from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = {i: i for i in range(1, len(edges) + 1)}
        self.rank = {i: 0 for i in range(1, len(edges) + 1)}

        def findParent(x: int) -> int:
            if not self.parent[x] == x:
                return findParent(self.parent[self.parent[x]])
            return x

        def union(x1: int, x2: int) -> bool:
            x1, x2 = findParent(x1), findParent(x2)

            if x1 == x2:
                return False

            if self.rank[x1] > self.rank[x2]:
                self.parent[x2] = x1
            elif self.rank[x1] < self.rank[x2]:
                self.parent[x1] = x2
            else:
                self.parent[x2] = x1
                self.rank[x1] -= 1

            return True

        for x1, x2 in edges:
            if not union(x1, x2):
                return [x1, x2]

        return [-1, -1]
