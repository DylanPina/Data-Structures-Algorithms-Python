from typing import List
from collections import defaultdict


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereqs = defaultdict(list)
        for prereq, course in prerequisites:
            prereqs[course].append(prereq)

        def dfs(course: int):
            if course not in prereqMap:
                for pre in prereqs[course]:
                    prereqMap[course] |= dfs(pre)
            prereqMap[course].add(course)
            return prereqMap[course]

        prereqMap = defaultdict(set)
        for crs in range(numCourses):
            dfs(crs)
        
        res = []
        for u, v in queries:
            res.append(u in prereqs[v])
        print(prereqMap)
        return res