from heapq import heappop, heappush
from typing import List


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []
        happy_chars = ["a", "b", "c"]

        def backtrack(cur: List[str]) -> None:
            if len(cur) == n:
                heappush(happy_strings, "".join(cur))
                return

            for c in happy_chars:
                if cur and cur[-1] == c:
                    continue

                cur.append(c)
                backtrack(cur)
                cur.pop()

        backtrack([])

        # If there are fewer than k strings, return empty string
        if len(happy_strings) < k:
            return ""

        # Get the kth smallest element
        for _ in range(k - 1):
            if happy_strings:
                heappop(happy_strings)
            else:
                return ""

        return heappop(happy_strings) if happy_strings else ""
