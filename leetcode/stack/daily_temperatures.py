from typing import List, Tuple


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[Tuple[int, int]] = []
        res: List[int] = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, i_prev = stack.pop()
                res[i_prev] = i - i_prev
            stack.append((t, i))
        return res
