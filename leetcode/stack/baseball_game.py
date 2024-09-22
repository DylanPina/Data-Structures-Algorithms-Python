from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for val in operations:
           match val:
                case '+':
                    s1, s2 = stack[-1], stack[-2]
                    stack.append(s1 + s2)
                case 'D':
                    s = stack[-1]
                    stack.append(s * 2)
                case 'C':
                    stack.pop()
                case _:
                    stack.append(int(val))
        return sum(stack)
