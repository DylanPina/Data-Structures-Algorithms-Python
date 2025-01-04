from typing import List
from heapq import heappop, heappush


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = sorted([(s, i) for i, s in enumerate(servers)])  # (Server weight, index)
        busy = []  # (Time Remaining, Server weight, index)
        res = []
        time = 0

        for i, task in enumerate(tasks):
            time = max(time, i)

            if not free:
                time = busy[0][0]

            while busy and time >= busy[0][0]:
                _, server, idx = heappop(busy)
                heappush(free, (server, idx))

            server, idx = heappop(free)
            heappush(busy, (time + task, server, idx))
            res.append(idx)

        return res
