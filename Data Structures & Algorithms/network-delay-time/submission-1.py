class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v,t))
        
        # Minheap has the pathTime, node. We take the min of the pathTime for Calc
        minHeap = [(0,k)]
        visited = set()
        time = 0

        while minHeap:
            pathTime, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            time = max(time, pathTime)

            for nei, neiTime in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (neiTime + pathTime, nei))
        
        return time if len(visited) == n else -1

        # DFS Approach
        # # Build adj list
        # adjList = defaultdict(list)
        # for u, v, t in times:
        #     adjList[u].append((v,t))
        
        # def dfs(node, time):
        #     if minTime[node] <= time:
        #         return 

        #     minTime[node] = time
        #     for nei, neiTime in adjList[node]:
        #         dfs(nei, time + neiTime)

        # minTime = {node: float("inf") for node in range(1,n+1)}
        # dfs(k, 0)

        # # Could not reach all nodes
        # if max(minTime.values()) == float("inf"):
        #     return -1
        # return max(minTime.values())