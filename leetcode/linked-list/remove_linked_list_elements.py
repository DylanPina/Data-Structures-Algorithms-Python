from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        res, cur = ListNode(0, head), head
        while cur != None:
            while cur.next and cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
        return res.next
