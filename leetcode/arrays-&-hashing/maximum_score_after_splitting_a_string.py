class Solution:
    def maxScore(self, s: str) -> int:
        right = 0
        for digit in s[1::]:
            if digit == "1":
                right += 1

        left = 1 if s[0] == "0" else 0
        res = right + left
        for digit in s[1:-1]:
            if digit == "0":
                left += 1
            else:
                right -= 1
            res = max(res, left + right)

        return res
