from typing import List
from heapq import heappush, heappop


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted([[start, end, passengers] for (passengers, start, end) in trips])
        ongoing = []

        for start, end, passengers in trips:
            while ongoing and ongoing[0][0] <= start:
                _, passengersLeaving = heappop(ongoing)
                capacity += passengersLeaving

            heappush(ongoing, (end, passengers))
            capacity -= passengers

            if capacity < 0:
                return False

        return True
