from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        prereqs = defaultdict(list)

        for course, prereq in prerequisites:
            prereqs[course].append(prereq)

        def dfs(cur: int) -> bool:
            if cur in visited:
                return False
            if not prereqs[cur]:
                return True

            visited.add(cur)
            for p in prereqs[cur]:
                if not dfs(p):
                    return False

            visited.remove(cur)
            prereqs[cur] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
