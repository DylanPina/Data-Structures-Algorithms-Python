class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_split = s.split(" ")
        if len(pattern) != len(s_split):
            return False

        pattern_map, s_map = {}, {}
        for a, b in zip(pattern, s_split):
            if (a in pattern_map and pattern_map[a] != b) or (
                b in s_map and s_map[b] != a
            ):
                return False
            pattern_map[a] = b
            s_map[b] = a
        return True
