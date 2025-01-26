from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
        if not len(trust):
            return 1

        trusts = {i: [] for i in range(1, n + 1)}
        trusted = {i: [] for i in range(1, n + 1)}

        for truster, trustee in trust:
            trusted[trustee].append(truster)
            trusts[truster].append(trustee)

        maxTrusted = (0, 0)
        for person, trustees in trusted.items():
            if len(trustees) > maxTrusted[0]:
                maxTrusted = (len(trustees), person)

        return (
            maxTrusted[1]
            if maxTrusted[0] == n - 1 and not len(trusts[maxTrusted[1]])
            else -1
        )
