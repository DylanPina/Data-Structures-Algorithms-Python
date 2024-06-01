from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        for a, _ in paths:
            s.add(a)
        for _, b in paths:
            if b not in s:
                return b
        return ""
