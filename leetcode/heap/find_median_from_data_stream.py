from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.small = []  # Max heap
        self.large = []  # Min heap

    def addNum(self, num: int) -> None:
        heappush(self.small, -1 * num)

        # Make sure every num small is <= every num in large
        if self.small and self.large and (-1 * self.small[0]) > self.large[0]:
            heappush(self.large, (-1 * heappop(self.small)))

        # Uneven size?
        if len(self.small) > len(self.large) + 1:
            heappush(self.large, -1 * heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heappush(self.small, -1 * heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return ((-1 * self.small[0]) + self.large[0]) / 2
