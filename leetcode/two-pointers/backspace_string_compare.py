class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def nextValidChar(s: str, i: int) -> int:
            backspace = 0
            while i >= 0:
                if backspace == 0 and s[i] != "#":
                    break
                elif s[i] == "#":
                    backspace += 1
                else:
                    backspace -= 1
                i -= 1
            return i

        s_i, t_i = len(s) - 1, len(t) - 1
        while s_i >= 0 or t_i >= 0:
            s_i = nextValidChar(s, s_i)
            t_i = nextValidChar(t, t_i)

            s_c = s[s_i] if s_i >= 0 else ""
            t_c = t[t_i] if t_i >= 0 else ""
            if s_c != t_c:
                return False
            s_i -= 1
            t_i -= 1
        return True
