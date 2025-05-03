from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * ((2 * n) - 1)
        used = set()

        def backtrack(i: int) -> bool:
            if i == len(res):
                return True

            for num in reversed(range(1, n + 1)):
                if num in used or (
                    (num != 1) and (i + num >= len(res) or res[i + num] != 0)
                ):
                    continue

                res[i] = num
                if num != 1:
                    res[i + num] = num
                used.add(num)

                j = i + 1
                while j < len(res) and res[j]:
                    j += 1

                if backtrack(j):
                    return True

                res[i] = 0
                if num != 1:
                    res[i + num] = 0
                used.remove(num)

            return False

        backtrack(0)
        return res
