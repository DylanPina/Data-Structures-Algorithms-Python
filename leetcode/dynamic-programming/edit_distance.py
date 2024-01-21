class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.dp(word1, word2)

    def dp(self, word1: str, word2: str) -> int:
        prev_row = [i for i in range(len(word2), -1, -1)]

        for r in range(len(word1) - 1, -1, -1):
            cur_row = [0] * (len(word2) + 1)
            cur_row[len(word2)] = len(word1) - r

            for c in range(len(word2) - 1, -1, -1):
                if word1[r] == word2[c]:
                    cur_row[c] = prev_row[c + 1]
                else:
                    cur_row[c] = min(cur_row[c + 1], prev_row[c], prev_row[c + 1]) + 1
            prev_row = cur_row

        return prev_row[0]


sol = Solution()
print(sol.minDistance("horse", "ros"))
