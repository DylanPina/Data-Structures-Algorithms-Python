from collections import defaultdict, deque


class Graph:

    def __init__(self):
        self.neighbors = defaultdict(list)

    def addEdge(self, src: int, dst: int) -> None:
        self.neighbors[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if dst not in self.neighbors[src]:
            return False

        self.neighbors[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        if src not in self.neighbors.keys():
            return False

        q = deque([src])
        visited = set([src])
        while q:
            for _ in range(len(q)):
                cur = q.popleft()

                if cur == dst:
                    return True

                for neighbor in self.neighbors[cur]:
                    if neighbor in visited:
                        continue
                    q.append(neighbor)
                    visited.add(neighbor)

        return False
