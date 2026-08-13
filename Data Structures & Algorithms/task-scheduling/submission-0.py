class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hmap = Counter(tasks)
        maxHeap = [-count for count in hmap.values()]
        heapq.heapify(maxHeap)

        queue = deque()   #Store the -ve count and the time it can be removed from being idle

        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)  #the cnt value is -ve or 0
                if cnt != 0:
                    queue.append((cnt, time+n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time