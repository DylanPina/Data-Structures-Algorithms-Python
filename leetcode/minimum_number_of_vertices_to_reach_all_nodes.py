from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list(set(range(n)) - {v for _, v in edges})
