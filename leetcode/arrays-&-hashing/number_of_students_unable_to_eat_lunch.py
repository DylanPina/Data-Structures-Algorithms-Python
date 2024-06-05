from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i = requed = 0
        while i < len(sandwiches):
            if requed == len(students):
                return len(sandwiches) - i

            if students[0] == sandwiches[i]:
                students.pop(0)
                i += 1
                requed = 0
            else:
                students.append(students.pop(0))
                requed += 1
        return 0
