from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case
        if not k or not head:
            return head

        # Get length of list
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if not k:
            return head

        cur = head
        for _ in range(length - k - 1):
            cur = cur.next
        res = cur.next
        cur.next = None
        tail.next = head

        return res
