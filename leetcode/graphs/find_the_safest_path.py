import heapq
from collections import deque
from typing import List, Tuple


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def neighbors(r: int, c: int) -> List[int]:
            return [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

        def in_bounds(r: int, c: int) -> bool:
            return min(r, c) >= 0 and max(r, c) < N

        def precompute() -> dict[Tuple[int, int], int]:
            q = deque()
            min_dist = {}

            for r in range(N):
                for c in range(N):
                    if grid[r][c]:
                        q.append([r, c, 0])
                        min_dist[(r, c)] = 0

            while q:
                r, c, dist = q.popleft()
                for r2, c2 in neighbors(r, c):
                    if in_bounds(r2, c2) and (r2, c2) not in min_dist:
                        min_dist[(r2, c2)] = dist + 1
                        q.append([r2, c2, dist + 1])

            return min_dist

        min_dist = precompute()
        maxHeap = [(-min_dist[(0, 0)], 0, 0)]  # (dist, r, c)
        visit = set([(0, 0)])

        while maxHeap:
            d, r, c = heapq.heappop(maxHeap)
            d = -d

            if (r, c) == (N - 1, N - 1):
                return d

            for r2, c2 in neighbors(r, c):
                if in_bounds(r2, c2) and (r2, c2) not in visit:
                    visit.add((r2, c2))
                    d2 = min(d, min_dist[(r2, c2)])
                    heapq.heappush(maxHeap, (-d2, r2, c2))
