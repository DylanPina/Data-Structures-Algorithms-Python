class Solution:
    def bestClosingTime(self, customers: str) -> int:
        yCount = customers.count("Y")
        res, minPenatly = 0, yCount

        cur = yCount
        for i, c in enumerate(customers):
            cur += -1 if c == "Y" else 1
            if cur < minPenatly:
                res, minPenatly = i + 1, cur
        return res
