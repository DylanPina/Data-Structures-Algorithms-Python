from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result, sequences = set(), set()
        for i in range(len(s) - 9):
            current = s[i : i + 10]
            if current in sequences:
                result.add(current)
            sequences.add(current)
        return list(result)
