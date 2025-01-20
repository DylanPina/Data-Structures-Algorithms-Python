from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqMap = defaultdict(list)
        for src, dst in prerequisites:
            prereqMap[src].append(dst)

        visiting = set()

        def dfs(cur: int) -> bool:
            if cur in visiting:
                return False

            if cur not in prereqMap:
                return True

            visiting.add(cur)
            for preq in prereqMap[cur]:
                if not dfs(preq):
                    return False

            visiting.remove(cur)
            del prereqMap[cur]
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
