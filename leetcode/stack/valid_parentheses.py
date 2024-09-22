class Solution:
    def isValid(self, s: str) -> bool:
        if not s or (len(s) % 2 != 0):
            return False

        stack = []
        map = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in map:
                if not stack or stack[-1] != map[c]:
                    return False
                else:
                    stack.pop()
            if c in map.values():
                stack.append(c)
        return not stack
