from heapq import heappop, heappush
from typing import List


class Solution:
    def maxPoints(self, g: List[List[int]], queries: List[int]) -> List[int]:
        ROWS, COLS = len(g), len(g[0])
        q = [(val, i) for i, val in enumerate(queries)]
        q.sort()

        min_heap = [(g[0][0], 0, 0)]
        visit = set([(0, 0)])
        res = [0] * len(q)
        points = 0

        for limit, i in q:
            while min_heap and min_heap[0][0] < limit:
                val, r, c = heappop(min_heap)
                points += 1

                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit:
                        heappush(min_heap, (g[nr][nc], nr, nc))
                        visit.add((nr, nc))
            res[i] = points

        return res
