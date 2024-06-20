class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        unique_codes = set()
        for i in range(len(s) - k + 1):
            unique_codes.add(s[i : i + k])
        return len(unique_codes) == (2**k)
