from collections import defaultdict


class FreqStack:

    def __init__(self):
        self.freq = defaultdict(list)  # [int -> stack]
        self.occurences = defaultdict(int)  # [int -> int]
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.occurences[val] += 1
        self.maxFreq = max(self.maxFreq, self.occurences[val])
        self.freq[self.occurences[val]].append(val)

    def pop(self) -> int:
        val = self.freq[self.maxFreq].pop()
        self.occurences[val] -= 1
        self.maxFreq -= 1 if not self.freq[self.maxFreq] else 0
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
