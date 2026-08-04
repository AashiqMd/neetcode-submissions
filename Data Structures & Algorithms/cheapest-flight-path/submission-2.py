class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u,v,d in flights:
            adj[u].append((v,d))
        optimal = [[float("inf")] * (k+2) for _ in range(n)]
        
        minheap = [(0, src, -1)] # cost, src , k
        while minheap:
            cst, node, stops = heapq.heappop(minheap)
            if node == dst:
                return cst
            if cst > optimal[node][stops+1] or stops >= k:
                continue
            
            for nei, ndist in adj[node]:
                ncst = cst+ndist
                nstops = stops + 1
                if ncst < optimal[nei][nstops+1]:
                    optimal[nei][nstops+1] = ncst
                    heapq.heappush(minheap, (cst+ndist, nei, stops+1))
        
        return -1