from collections import deque
from typing import List


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        roads = {i: [i + 1] for i in range(n)}

        def bfs() -> int:
            q = deque([0])
            visited = set()
            distance = 0

            while q:
                for _ in range(len(q)):
                    cur = q.popleft()
                    visited.add(cur)

                    for road in roads[cur]:
                        if road == n - 1:
                            return distance + 1

                        if road not in visited:
                            q.append(road)
                distance += 1

            return -1

        res = []
        for u, v in queries:
            roads[u].append(v)
            res.append(bfs())
        return res
