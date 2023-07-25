from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = self.getKth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            # reverse group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                next = curr.next,
                curr.next = prev
                prev = curr
                curr = next

            group_prev_next = group_prev.next
            group_prev.next = kth
            group_prev = group_prev_next

        return dummy.next

    def getKth(self, curr: ListNode, k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
