class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map, t_map = {}, {}

        for s_i, t_i in zip(s, t):
            if (s_i in s_map and s_map[s_i] != t_i) or (
                t_i in t_map and t_map[t_i] != s_i
            ):
                return False
            s_map[s_i] = t_i
            t_map[t_i] = s_i

        return True
