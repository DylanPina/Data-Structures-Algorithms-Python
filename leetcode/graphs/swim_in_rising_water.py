from typing import List
from heapq import heappop, heappush


class Solution:
    def swimInWater(self, g: List[List[int]]) -> int:
        M, N = len(g), len(g[0])
        minHeap = [(g[0][0], 0, 0)]  # elevation, row, column
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        while minHeap:
            elevation, r, c = heappop(minHeap)
            if r == M - 1 and c == N - 1:
                return elevation
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < M and 0 <= nc < N and (nr, nc) not in visited:
                    heappush(minHeap, (max(elevation, g[nr][nc]), nr, nc))

        return -1
