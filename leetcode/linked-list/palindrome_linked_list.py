from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Slow fast pointer to reverse second half of the list
        if not head:
            return False
        if not head.next:
            return True

        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        l, r = head, prev
        while l and r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
