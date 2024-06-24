from collections import defaultdict
from typing import Tuple


class UndergroundSystem:

    def __init__(self):
        self.checkInMap = defaultdict(Tuple)
        self.totalMap = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        inStation, inTime = self.checkInMap[id]
        route = (inStation, stationName)
        if not route in self.totalMap:
            self.totalMap[route] = [0, 0]
        self.totalMap[route][0] += t - inTime
        self.totalMap[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, trips = self.totalMap[(startStation, endStation)]
        return totalTime / trips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
