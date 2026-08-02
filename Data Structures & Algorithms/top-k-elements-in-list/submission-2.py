class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            freqMap[num]+=1

        for key, v in freqMap.items():
            freq[v].append(key)
        
        res = []
        for i in range(len(freq)-1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

        # freq = defaultdict(int)
        # for num in nums:
        #     freq[num]+=1
        
        # minheap = []

        # for key,v in freq.items():
        #     heapq.heappush(minheap,(v,key))
        #     if len(minheap) > k:
        #         heapq.heappop(minheap)
        
        # res = []
        # for i in range(k):
        #     key, value = heapq.heappop(minheap)
        #     res.append(value)
        
        return res