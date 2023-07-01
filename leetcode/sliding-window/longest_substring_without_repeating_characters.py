class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        L = 0
        chars = set()

        for R in range(len(s)):
            while s[R] in chars:
                chars.remove(s[L])
                L += 1
            length = max(length, R - L + 1)
            chars.add(s[R])
            
        return length
