from collections import defaultdict
from typing import List


class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        secrets = set([0, firstPerson])

        time_map = {}  # time -> adj[list of meetings]
        for src, dst, time in meetings:
            if time not in time_map:
                time_map[time] = defaultdict(list)
            time_map[time][src].append(dst)
            time_map[time][dst].append(src)

        def dfs(node: int, adj: defaultdict) -> None:
            if node in visit:
                return

            visit.add(node)
            secrets.add(node)

            for nei in adj[node]:
                dfs(nei, adj)

        for time in sorted(time_map.keys()):
            visit = set()
            for node in time_map[time]:
                if node in secrets:
                    dfs(node, time_map[time])

        return list(secrets)
