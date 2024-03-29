import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-num for num in nums]
        heapq.heapify(maxHeap)
        
        kthLargest = maxHeap[0] if maxHeap else 0
        for _ in range(k):
            kthLargest = heapq.heappop(maxHeap)
            
        return -1 * kthLargest