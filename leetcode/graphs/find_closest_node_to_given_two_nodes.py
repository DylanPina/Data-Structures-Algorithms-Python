from typing import List


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def dfs(node, dist):
            nei = edges[node]
            if nei != -1 and dist[nei] == -1:
                dist[nei] = dist[node] + 1
                dfs(nei, dist)

        node1Dist = [-1] * n
        node2Dist = [-1] * n
        node1Dist[node1] = node2Dist[node2] = 0

        dfs(node1, node1Dist)
        dfs(node2, node2Dist)

        res, resDist = -1, float("inf")
        for i in range(n):
            if min(node1Dist[i], node2Dist[i]) != -1:
                dist = max(node1Dist[i], node2Dist[i])
                if dist < resDist:
                    resDist, res = dist, i

        return res
