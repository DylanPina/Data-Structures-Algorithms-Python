from heapq import heappop, heappush


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, maxHeap = [], []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heappush(maxHeap, (count, char))

        while maxHeap:
            count, char = heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heappop(maxHeap)
                res.append(char2)
                count2 += 1
                if count2:
                    heappush(maxHeap, (count2, char2))
            else:
                res += char
                count += 1

            if count:
                heappush(maxHeap, (count, char))

        return "".join(res)
