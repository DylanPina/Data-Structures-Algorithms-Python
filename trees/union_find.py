class UnionFind:

    def __init__(self, n: int):
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}
        self.components = n

    def find(self, x: int) -> int:
        if not self.parent[x] == x:
            return self.find(self.parent[x])
        return x

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)

        if x == y:
            return False

        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            self.rank[x] += 1

        self.components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.components
