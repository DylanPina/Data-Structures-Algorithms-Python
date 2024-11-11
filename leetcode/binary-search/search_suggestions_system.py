from typing import List


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        res = []
        products.sort()

        l, r = 0, len(products) - 1
        for i, c in enumerate(searchWord):
            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1

            remaining = r - l + 1
            res.append(products[l : min(3, remaining) + l])
        return res
