from typing import List


class Solution:
    def regionsBySlashes(self, g: List[str]) -> int:
        R1, C1 = len(g), len(g[0])
        R2, C2 = R1 * 3, C1 * 3
        g2 = [[0] * C2 for _ in range(R2)]

        # build g2
        for i, row in enumerate(g):
            for j, ch in enumerate(row):
                # compute the top‐left corner of the 3×3 block
                r0, c0 = i * 3, j * 3

                for dr in range(3):
                    for dc in range(3):
                        if ch == "/":
                            if dr + dc == 2:
                                g2[r0 + dr][c0 + dc] = 1
                        elif ch == "\\":
                            if dr == dc:
                                g2[r0 + dr][c0 + dc] = 1

        def dfs(r: int, c: int):
            g2[r][c] = 1
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= nr < R2 and 0 <= nc < C2 and g2[nr][nc] == 0:
                    dfs(nr, nc)

        regions = 0

        for r in range(R2):
            for c in range(C2):
                if not g2[r][c]:
                    dfs(r, c)
                    regions += 1

        return regions
