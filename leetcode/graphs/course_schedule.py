from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) > numCourses:
            return False

        prereqMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)

        visiting = set()

        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            if not prereqMap[course]:
                return True

            visiting.add(course)

            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            prereqMap[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
