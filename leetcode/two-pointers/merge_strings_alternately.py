class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        j = k = 0

        while j < len(word1) and k < len(word2):
            if j <= k:
                res += word1[j]
                j += 1
            else:
                res += word2[k]
                k += 1

        while j < len(word1):
            res += word1[j]
            j += 1

        while k < len(word2):
            res += word2[k]
            k += 1

        return res
