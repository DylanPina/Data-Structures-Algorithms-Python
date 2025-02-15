from typing import List


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        prereqMap = {course: [] for course in range(numCourses)}
        memo = [[-1 for _ in range(numCourses)] for _ in range(numCourses)]

        for prereq, course in prerequisites:
            prereqMap[course].append(prereq)
            memo[course][prereq] = True

        def dfs(course: int, prereq: int) -> bool:
            if memo[course][prereq] != -1:
                return bool(memo[course][prereq])

            for prereq in prereqMap[course]:
                if dfs(prereq, prereq):
                    memo[course][prereq] = 1
                    return True

            memo[course][prereq] = 0
            return False

        res = []
        for prereq, course in queries:
            if course == prereq:
                res.append(False)
            else:
                res.append(dfs(course, prereq))
        return res
