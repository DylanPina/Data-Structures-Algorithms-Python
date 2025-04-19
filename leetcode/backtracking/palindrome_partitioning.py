from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        palindromes, partition = [], []

        def dfs(i: int) -> None:
            if i == len(s):
                palindromes.append(partition.copy())
                return

            for j in range(i, len(s)):
                if self.palindrome(s[i : j + 1]):
                    partition.append(s[i : j + 1])
                    dfs(j + 1)
                    partition.pop()

        dfs(0)
        return palindromes

    def palindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True
