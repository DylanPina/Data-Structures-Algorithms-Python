class Solution:
    def minSwaps(self, s: str) -> int:
        close = maxClose = 0
        for c in s:
            close += 1 if c == "]" else -1
            maxClose = max(close, maxClose)
        return (maxClose + 1) // 2
