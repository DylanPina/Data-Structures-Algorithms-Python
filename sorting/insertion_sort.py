from typing import List


class InsertionSort:
    def sort(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            j = i - 1
            while (j >= 0) and (arr[j + 1] < arr[j]):
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
                j -= 1

        return arr
