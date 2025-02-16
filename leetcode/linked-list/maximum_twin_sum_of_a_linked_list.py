from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find the mid point
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        # Reverse second half of the list
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        right = prev

        # Add 'twins'
        max_pair_sum = float("-inf")
        left = head
        while left and right:
            max_pair_sum = max(max_pair_sum, left.val + right.left)
            left = left.next
            right = right.next

        return max_pair_sum
