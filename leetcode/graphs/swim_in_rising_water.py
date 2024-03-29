from typing import List
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        minheap = []
        heapq.heappush(minheap, [grid[0][0], 0, 0])  # [elevation, r, c]

        t = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while heapq:
            e, r, c = heapq.heappop(minheap)
            if (r, c) in visited:
                continue

            t = max(t, e)
            if r == len(grid) - 1 and c == len(grid) - 1:
                return t

            visited.add((r, c))
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row in range(len(grid)) and col in range(len(grid)):
                    heapq.heappush(minheap, [grid[row][col], row, col])
        return t
