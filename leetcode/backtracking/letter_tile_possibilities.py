from typing import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def dfs() -> int:
            res = 0

            for ch in count:
                if count[ch] == 0:
                    continue

                count[ch] -= 1
                res += dfs() + 1

                count[ch] += 1

            return res

        return dfs()
