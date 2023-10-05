from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqs = defaultdict(list)
        path, visited = set(), set()
        res = []

        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        def dfs(curr: int) -> bool:
            if curr in path:
                return False
            if curr in visited:
                return True

            path.add(curr)
            for prereq in prereqs[curr]:
                if not dfs(prereq):
                    return False
            path.remove(curr)
            visited.add(curr)
            res.append(curr)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
