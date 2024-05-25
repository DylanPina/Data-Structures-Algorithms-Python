from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return n == len(flowerbed) and flowerbed[0] == 0 or n == 0

        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
            elif (
                i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0
            ):
                n -= 1
                flowerbed[i] = 1
            elif flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
        return n <= 0
