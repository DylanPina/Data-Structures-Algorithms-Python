class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if not self.capacity:
            return False

        newNode = ListNode(value)
        if not self.head:
            self.head = self.tail = newNode
            self.head.next = self.tail
        else:
            self.tail.next = newNode
            self.tail = self.tail.next

        self.capacity -= 1
        return True

    def deQueue(self) -> bool:
        if not self.head:
            return False

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next

        self.capacity += 1
        return True

    def Front(self) -> int:
        return self.head.val if self.head else -1

    def Rear(self) -> int:
        return self.tail.val if self.tail else -1

    def isEmpty(self) -> bool:
        return not self.head

    def isFull(self) -> bool:
        return not self.capacity
