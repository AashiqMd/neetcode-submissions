class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        minheap = []

        for key,v in freq.items():
            # v = freq[key]
            if len(minheap) < k:
                heapq.heappush(minheap, (v,key))
            else:
                if minheap[0][0] < v:
                    heapq.heappop(minheap)
                    heapq.heappush(minheap, (v,key))
        
        res = []
        while len(minheap) >0:
            res.append(heapq.heappop(minheap)[1])
        return res