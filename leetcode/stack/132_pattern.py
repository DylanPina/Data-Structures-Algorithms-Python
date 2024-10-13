from typing import List


class Solution:
    def find132pattern(self, N: List[int]) -> bool:
        stack = []  # (num, min)
        curMin = N[0]

        for n in N:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n < stack[-1][0] and n > stack[-1][1]:
                return True

            curMin = min(curMin, n)
            stack.append([n, curMin])
        return False

    def bruteForce(self, N: List[int]) -> bool:
        for i in range(len(N) - 2):
            j = i + 1
            while j < len(N) - 1 and N[j] <= N[i]:
                j += 1
            if j == len(N) - 1:
                continue

            k = j + 1
            while k < len(N) and not (N[i] < N[k] and N[k] < N[j]):
                k += 1
            if k == len(N):
                continue

            return True
        return False
