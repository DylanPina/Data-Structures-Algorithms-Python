from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Quick check: total perimeter must be divisible by 4
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False

        target = perimeter // 4
        sides = [0] * 4

        # Sort in descending order for faster pruning
        matchsticks.sort(reverse=True)

        def backtrack(i: int) -> bool:
            # Base case: all matchsticks used
            if i == len(matchsticks):
                return all(side == target for side in sides)

            # Try placing current matchstick in each side
            for s in range(4):
                # Skip if this would make identical choices (optimization)
                if s > 0 and sides[s] == sides[s - 1]:
                    continue

                # Skip if adding would exceed target
                if sides[s] + matchsticks[i] > target:
                    continue

                # Place matchstick and continue
                sides[s] += matchsticks[i]
                if backtrack(i + 1):
                    return True

                # Backtrack if not successful
                sides[s] -= matchsticks[i]

            return False

        return backtrack(0)
