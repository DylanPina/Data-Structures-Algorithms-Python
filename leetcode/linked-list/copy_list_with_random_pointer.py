from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        node_map = { None: None }

        cur = head
        while cur:
            copy = Node(cur.val)
            node_map[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = node_map[cur]
            copy.next = node_map[cur.next]
            copy.random = node_map[cur.random]
            cur = cur.next

        return node_map[head]
