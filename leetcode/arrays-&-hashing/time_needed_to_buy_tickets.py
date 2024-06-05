from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for i, ticket in enumerate(tickets):
            if i <= k:
                res += min(ticket, tickets[k])
            else:
                res += min(ticket, tickets[k] - 1)
        return res
