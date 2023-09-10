from typing import List


class QuickSort:
    def sort(self, arr: List[int]) -> List[int]:
        return self.quickSort(arr, 0, len(arr) - 1)

    def quickSort(self, arr: List[int], s: int, e: int) -> List[int]:
        if e - s + 1 <= 1:
            return arr

        pivot = arr[e]
        left = s

        for i in range(s, e):
            if arr[i] < pivot:
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1

        arr[e] = arr[left]
        arr[left] = pivot

        self.quickSort(arr, s, left - 1)
        self.quickSort(arr, left + 1, e)
        return arr
