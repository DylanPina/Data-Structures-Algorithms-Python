class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return self.validPalindromeUtil(
                    s, l + 1, r
                ) or self.validPalindromeUtil(s, l, r - 1)
            l += 1
            r -= 1
        return True

    def validPalindromeUtil(self, s: str, l: int, r: int):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
