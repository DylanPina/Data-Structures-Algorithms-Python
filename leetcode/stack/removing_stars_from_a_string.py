class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for s_i in s:
            if s_i == "*":
                stack.pop()
            else:
                stack.append(s_i)
        return "".join(stack)
