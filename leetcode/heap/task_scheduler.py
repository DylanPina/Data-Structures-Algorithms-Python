from collections import Counter, deque
from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [-count for count in Counter(tasks).values()]
        heapify(maxHeap)

        time = 0
        coolDown = deque()
        while maxHeap or coolDown:
            time += 1

            if maxHeap:
                # Process the most frequent task
                if (count := heappop(maxHeap)) + 1:
                    coolDown.append((count + 1, time + n))

            # Handle cooldowns
            if coolDown and coolDown[0][1] == time:
                heappush(maxHeap, coolDown.popleft()[0])

        return time
