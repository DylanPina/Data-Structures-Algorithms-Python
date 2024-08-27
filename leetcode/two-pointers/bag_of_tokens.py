from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        maxScore = score = 0
        tokens.sort()
        l, r = 0, len(tokens) - 1

        while l <= r:
            if tokens[l] <= power:
                power -= tokens[l]
                score += 1
                maxScore = max(maxScore, score)
                l += 1
            elif score:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
        return maxScore
