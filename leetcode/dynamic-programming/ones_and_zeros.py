from collections import defaultdict
from typing import Dict, List, Tuple


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.dp(strs, m, n)

    def dp(self, strs: List[str], M: int, N: int) -> int:
        dp: Dict[Tuple[int, int], int] = defaultdict(int)

        for s in strs:
            m_count, n_count = s.count("0"), s.count("1")
            for m in range(M, m_count - 1, -1):
                for n in range(N, n_count - 1, -1):
                    dp[(m, n)] = max(1 + dp[(m - m_count, n - n_count)], dp[(m, n)])
        return dp[(M, N)]

    def memoization(self, strs: List[str], m: int, n: int) -> int:
        dp: Dict[Tuple[int, int, int], int] = {}

        def dfs(i: int, m: int, n: int) -> int:
            if i == len(strs):
                return 0
            if (i, m, n) in dp:
                return dp[(i, m, n)]

            m_count, n_count = strs[i].count("0"), strs[i].count("1")
            dp[(i, m, n)] = dfs(i + 1, m, n)

            if m_count <= m and n_count <= n:
                dp[(i, m, n)] = max(
                    dp[(i, m, n)], 1 + dfs(i + 1, m - m_count, n - n_count)
                )
            return dp[(i, m, n)]

        return dfs(0, m, n)
