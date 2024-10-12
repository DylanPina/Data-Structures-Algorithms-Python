class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # (count, char)

        for s_i in s:
            if stack and s_i == stack[-1][1]:
                stack[-1][0] += 1
            else:
                stack.append([1, s_i])

            if stack[-1][0] == k:
                stack.pop()

        res = ""
        for count, char in stack:
            res += char * count
        return res
