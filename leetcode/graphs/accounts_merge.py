from typing import List
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        unionFind = UnionFind(len(accounts))
        emailToAcc = {}  # email -> index of acc

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    unionFind.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        emailGroup = defaultdict(list)  # index acc -> list of emails
        for e, i in emailToAcc.items():
            leader = unionFind.find(i)
            emailGroup[leader].append(e)

        res = []
        for i in emailGroup.keys():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))  # array concat
        return res


class UnionFind:
    def __init__(self, n: int):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        x_root, y_root = self.find(x), self.find(y)

        if x_root != y_root:
            if self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
                self.rank[y_root] += self.rank[x_root]
            else:
                self.parent[y_root] = x_root
                self.rank[x_root] += self.rank[y_root]
            return True
        return False
