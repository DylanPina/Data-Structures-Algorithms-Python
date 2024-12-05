from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, cur = dummy, head
        for _ in range(left - 1):
            prev, cur = cur, cur.next
        l1Break, l2Start = prev, cur

        prev = None
        for _ in range((right - left) + 1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        l1Break.next = prev
        l2Start.next = cur
        return dummy.next
