from typing import List


class Solution:
    def maxLength(self, a: List[str]) -> int:
        def backtrack(i: int, chars: set[str]) -> None:
            if i == len(a):
                return len(chars)

            res = 0
            if not any(c in chars for c in a[i]) and len(set(a[i])) == len(a[i]):
                chars.update(a[i])
                res = backtrack(i + 1, chars)
                chars.difference_update(a[i])

            return max(res, backtrack(i + 1, chars))

        return backtrack(0, set())
