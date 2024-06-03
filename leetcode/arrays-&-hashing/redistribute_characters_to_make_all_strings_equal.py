from typing import List
from collections import Counter


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        char_to_freq = Counter(c for w in words for c in w)
        return all(freq % len(words) == 0 for freq in char_to_freq.values())
