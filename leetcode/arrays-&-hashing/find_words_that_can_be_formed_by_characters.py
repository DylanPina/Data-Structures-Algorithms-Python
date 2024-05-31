from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum(len(word) for word in words if all(word.count(char) <= chars.count(char) for char in set(word)))
