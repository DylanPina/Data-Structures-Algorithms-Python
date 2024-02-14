from typing import Dict, List
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count: Dict[int, int] = {}
        for card in hand:
            count[card] = 1 + count.get(card, 0)

        min_heap = list(count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            first = min_heap[0]

            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True


sol = Solution()
print(sol.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
