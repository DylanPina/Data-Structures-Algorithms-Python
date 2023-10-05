from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]

        def dfs(cur: str) -> None:
            if len(res) == len(tickets) + 1:
                return True
            if cur not in adj:
                return False

            for v in adj[cur].copy():
                adj[cur].popleft()
                res.append(v)
                if dfs(v):
                    return True
                adj[cur].append(v)
                res.pop()
            return False

        dfs("JFK")
        return res
