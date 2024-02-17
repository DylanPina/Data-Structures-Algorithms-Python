from typing import Dict, List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence_map: Dict[str, int] = {}
        for i, c in enumerate(s):
            last_occurence_map[c] = i

        res: List[int] = []
        size = last_occurence = 0
        for i, c in enumerate(s):
            last_occurence = max(last_occurence, last_occurence_map[c])
            size += 1

            if i == last_occurence:
                res.append(size)
                size = 0
        return res
