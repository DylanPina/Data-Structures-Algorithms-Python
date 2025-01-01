class Heap:
    def __init__(self):
        self.heap = []

    def push(self, value: int) -> None:
        self.heap.append(value)
        i = len(self) - 1

        # Percolate up
        while i > 0 and self.heap[i] < self.heap[parentIndex := self.parent(i)]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[parentIndex]
            self.heap[parentIndex] = tmp
            i = parentIndex

    def pop(self) -> int | None:
        if not len(self):
            return None
        if len(self) == 1:
            return self.heap.pop()

        res = self.heap[0]
        # Move the last value to the root
        self.heap[0] = self.heap.pop()

        # Percolate down
        i = 0
        while self.leftChild(i) < len(self):
            if (
                self.rightChild(i) < len(self)
                and self.heap[self.rightChild(i)] < self.heap[self.leftChild(i)]
            ) and self.heap[i] > self.heap[self.rightChild(i)]:
                # Swap right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[self.rightChild(i)]
                self.heap[self.rightChild(i)] = tmp
                i = self.rightChild(i)
            elif self.heap[i] > self.heap[self.leftChild(i)]:
                # Swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[self.leftChild(i)]
                self.heap[self.leftChild(i)] = tmp
                i = self.leftChild(i)
            else:
                break

        return res

    def heapify(self, arr: list[int]) -> list[int]:
        if not arr:
            return []

        self.heap = arr
        # Backwards from the middle of the array to the beginning
        for i in range((len(arr) - 1) // 2, -1, -1):
            # Percolate down
            while self.leftChild(i) < len(self):
                if (
                    self.rightChild(i) < len(self)
                    and self.heap[self.rightChild(i)] < self.heap[self.leftChild(i)]
                ) and self.heap[i] > self.heap[self.rightChild(i)]:
                    # Swap right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[self.rightChild(i)]
                    self.heap[self.rightChild(i)] = tmp
                    i = self.rightChild(i)
                elif self.heap[i] > self.heap[self.leftChild(i)]:
                    # Swap left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[self.leftChild(i)]
                    self.heap[self.leftChild(i)] = tmp
                    i = self.leftChild(i)
                else:
                    break
        return self.heap

    def peek(self) -> int | None:
        return self.heap[0] if len(self) else None

    def clear(self) -> None:
        self.heap = []

    def parent(self, childIndex: int) -> int:
        return (childIndex - 1) // 2

    def leftChild(self, parentIndex: int) -> int:
        return parentIndex * 2 + 1

    def rightChild(self, parentIndex: int) -> int:
        return parentIndex * 2 + 2

    def __len__(self) -> int:
        return len(self.heap)
