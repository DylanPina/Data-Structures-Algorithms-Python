from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums = set(nums)
        res = ""

        def backtrack(cur: List[str]) -> bool:
            nonlocal res

            if len(cur) == len(nums):
                if (s := "".join(cur)) not in nums:
                    res = s
                    return True
                return False

            cur.append("0")
            if backtrack(cur):
                return True
            cur.pop()

            cur.append("1")
            if backtrack(cur):
                return True
            cur.pop()

            return False

        backtrack([])
        return res
