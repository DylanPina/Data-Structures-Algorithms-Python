from typing import List


class MergeSort:
    def sort(self, arr: List[int]) -> List[int]:
        return self.mergeSort(arr, 0, len(arr) - 1)

    def mergeSort(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr

        m = (s + e) // 2
        self.mergeSort(arr, s, m)
        self.mergeSort(arr, m + 1, e)
        self.merge(arr, s, m, e)

        return arr

    def merge(self, arr: List[int], s: int, m: int, e: int) -> None:
        L, R = arr[s : m + 1], arr[m + 1 : e + 1]
        i = j = 0
        k = s

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
