class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        directions = {"N": [0, 1], "S": [0, -1], "E": [1, 0], "W": [-1, 0]}
        x, y = 0, 0

        for direction in path:
            visited.add((x, y))
            dx, dy = directions[direction]
            x, y = x + dx, y + dy

            if (x, y) in visited:
                return True
        return False
