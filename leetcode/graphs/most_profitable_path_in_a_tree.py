from collections import defaultdict, deque
from typing import List


class Solution:
    def mostProfitablePath(
        self, edges: List[List[int]], bob: int, amount: List[int]
    ) -> int:
        # Create an adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Calculate Bob's fixed path
        bob_visited = {}

        def bob_dfs(u: int, parent: int, time=0) -> bool:
            if u == 0:
                bob_visited[u] = time
                return True

            for v in adj[u]:
                if v == parent:
                    continue
                if bob_dfs(v, u, time + 1):
                    bob_visited[u] = time
                    return True

            return False

        bob_dfs(bob, -1)

        # Alice's simulation
        q = deque([(0, 0, -1, amount[0])])  # (node, time, parent, total profit)
        res = float("-inf")

        while q:
            for _ in range(len(q)):
                node, time, parent, profit = q.popleft()

                for v in adj[node]:
                    if v == parent:
                        continue

                    v_profit = amount[v]
                    v_time = time + 1

                    if v in bob_visited:
                        if bob_visited[v] == v_time:
                            v_profit /= 2
                        elif bob_visited[v] < v_time:
                            v_profit = 0

                    q.append((v, time + 1, node, profit + v_profit))

                    if len(adj[v]) == 1:
                        res = max(res, profit + v_profit)

        return int(res)
