from collections import defaultdict, deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # Create an adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Find all the leaf nodes
        edge_count, leaf_nodes = {}, deque()
        for node, neighbors in adj.items():
            edge_count[node] = len(neighbors)
            if len(neighbors) == 1:
                leaf_nodes.append(node)

        # Level out starting from leaf nodes
        while leaf_nodes:
            if n <= 2:
                return list(leaf_nodes)

            for _ in range(len(leaf_nodes)):
                node = leaf_nodes.popleft()
                n -= 1

                for nei in adj[node]:
                    edge_count[nei] -= 1

                    if edge_count[nei] == 1:
                        leaf_nodes.append(nei)

        return []
