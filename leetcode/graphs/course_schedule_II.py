from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not len(prerequisites):
            return list(range(numCourses))

        prereqMap = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)

        output = []
        visited, visiting = set(), set()

        def dfs(course: int) -> bool:
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)
            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            visited.add(course)
            output.append(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return output
