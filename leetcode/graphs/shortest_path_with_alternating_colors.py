from collections import defaultdict, deque
from typing import List

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redAdj, blueAdj = defaultdict(list), defaultdict(list)

        for u, v in redEdges:
            redAdj[u].append(v)
        for u, v in blueEdges:
            blueAdj[u].append(v)

        q = deque([(0, "blue"), (0, "red")])
        visited = set()
        res = [-1] * n

        distance = 0
        while q:
            for _ in range(len(q)):
                u, color = q.popleft()
                res[u] = min(res[u], distance) if res[u] != -1 else distance

                if color == "red":
                    for v in blueAdj[u]:
                        if (u, v, "blue") not in visited:
                            visited.add((u, v, "blue"))
                            q.append((v, "blue"))
                elif color == "blue":
                    for v in redAdj[u]:
                        if (u, v, "red") not in visited:
                            visited.add((u, v, "red"))
                            q.append((v, "red"))

            distance += 1
        return res