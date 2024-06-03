class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 1:
            return 0

        i = 0
        count = 0
        while i < len(s):
            if i % 2 == 0:
                if s[i] == "1":
                    count += 1
            else:
                if s[i] == "0":
                    count += 1
            i += 1
        return min(count, len(s) - count)
