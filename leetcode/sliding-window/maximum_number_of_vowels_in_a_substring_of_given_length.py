class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]

        res = count = l = 0
        for r in range(len(s)):
            count += 1 if s[r] in vowels else 0
            if r >= k:
                count -= 1 if s[l] in vowels else 0
                l += 1
            res = max(res, count)
        return res
