class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)

        if (len(self.maxheap) - len(self.minheap) >= 2) or (self.minheap and (-self.maxheap[0] > self.minheap[0])):
            temp = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, temp)

        if (len(self.minheap) - len(self.maxheap) >= 1):
            temp = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -temp)

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] - self.maxheap[0])/2
        else:
            return -self.maxheap[0]
        
        