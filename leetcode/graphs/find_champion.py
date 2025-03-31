from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Count the number of incoming edges
        adj = [0] * n
        for _, v in edges:
            adj[v] += 1

        champion = -1
        for i, v in enumerate(adj):
            if v == 0:
                if champion != -1:
                    return -1
                champion = i

        return champion
