class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.minheap = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        
        if len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
