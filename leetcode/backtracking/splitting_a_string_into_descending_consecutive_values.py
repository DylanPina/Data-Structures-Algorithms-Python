from typing import List


class Solution:
    def splitString(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        def backtrack(i: int, substrings: List[int]) -> bool:
            if i == len(s):
                return self.isDescendingOrder(substrings)

            for j in range(i, len(s)):
                substrings.append(int(s[i : j + 1]))

                if backtrack(j + 1, substrings):
                    return True

                substrings.pop()

            return False

        return backtrack(0, [])

    def isDescendingOrder(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False

        prev = None
        for n in nums:
            if prev is not None and prev != n + 1:
                return False
            prev = n
        return True
