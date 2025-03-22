from collections import defaultdict
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Create the adjacency list
        adj = defaultdict(list)
        for i, (x_i, y_i, r_i) in enumerate(bombs):
            # Check every other bomb to see if it's in blast radius
            for j, (x_j, y_j, _) in enumerate(bombs):
                # Ignore if it's the same bomb
                if i == j:
                    continue

                # If the bomb is in radius (Euclidean distance)
                if (x_i - x_j) ** 2 + (y_i - y_j) ** 2 <= r_i**2:
                    adj[(x_i, y_i)].append((x_j, y_j))

        def dfs(x_i: int, y_i: int, visited: set) -> int:
            visited.add((x_i, y_i))
            for x_j, y_j in adj[(x_i, y_i)]:
                if (x_j, y_j) not in visited:
                    dfs(x_j, y_j, visited)
            return len(visited)

        max_detonated = 0

        for x_i, y_i, _ in bombs:
            max_detonated = max(max_detonated, dfs(x_i, y_i, set()))

        return max_detonated
