class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        
        minheap = []

        for key,v in freq.items():
            heapq.heappush(minheap,(v,key))
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        res = []
        for i in range(k):
            key, value = heapq.heappop(minheap)
            res.append(value)
        
        return res