from collections import deque
from typing import List


class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.locked = [-1] * len(parent)
        self.child = {i: [] for i in range(len(parent))}
        for i in range(1, len(parent)):
            self.child[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num] != -1:  # Check if the node is already locked
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:  # Check if the node is locked by the same user
            return False
        self.locked[num] = -1  # Unlock the node
        return True

    def upgrade(self, num: int, user: int) -> bool:
        # Check all ancestors are unlocked
        cur = num
        while cur != -1:
            if self.locked[cur] != -1:  # If any ancestor is locked, return False
                return False
            cur = self.parent[cur]

        # Check if there is at least one locked descendant
        has_locked_descendant = False
        q = deque([num])
        while q:
            cur = q.popleft()
            if self.locked[cur] != -1:  # If the current node is locked
                self.locked[cur] = -1  # Unlock it
                has_locked_descendant = True
            q.extend(self.child[cur])  # Add children to the queue

        # If there is no locked descendant, return False
        if not has_locked_descendant:
            return False

        # Lock the current node
        self.locked[num] = user
        return True
