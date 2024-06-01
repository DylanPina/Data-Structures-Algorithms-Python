class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest, prev, count = -1, num[0], 1
        for digit in num[1::]:
            if digit == prev:
                count += 1
            else:
                count = 1
            if count == 3:
                largest = max(largest, int(digit))
            prev = digit
        return f"{largest}{largest}{largest}" if largest != -1 else ""
