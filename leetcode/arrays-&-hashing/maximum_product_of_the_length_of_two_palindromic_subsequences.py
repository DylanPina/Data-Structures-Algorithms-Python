class Solution:
    def maxProduct(self, s: str) -> int:
        n, pali = len(s), {}  # bitmask : length
        for mask in range(1, 1 << n):
            subseq = ""
            for i in range(n):
                if mask & (1 << i):
                    subseq += s[i]
            if subseq == subseq[::-1]:  # valid is palindromic
                pali[mask] = len(subseq)
        res = 0
        for mask1, length1 in pali.items():
            for mask2, length2 in pali.items():
                if mask1 & mask2 == 0:
                    res = max(res, length1 * length2)
        return res
