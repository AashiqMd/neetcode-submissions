class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra Approach
        # BFS using a priority queue
        adj = defaultdict(list)
        for u,v,t in times:
             adj[u].append((v,t))
            
        # Has the pathTime, node
        minHeap = [(0,k)]
        visited = set()
        res = 0

        # The idea is if I pull the min path length each time i.e. (1,5) and then (3,5), I can disregard (3,5)
        # Same node, more time
        while minHeap:
            pathTime, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            res = max(res, pathTime)

            for nei, neiTime in adj[node]:
                heapq.heappush(minHeap, (neiTime + pathTime, nei))
        
        return res if len(visited) == n else -1
        
        # # DFS Approach
        # adj = defaultdict(list)
        # for u,v,t in times:
        #     adj[u].append((v,t))
        
        # nodeTime = {node: float("inf") for node in range(1,n+1)}

        # # node and time is the current node and current time i.e. pathLength
        # def dfs(node, time):
        #     if time >= nodeTime[node]:
        #         return 

        #     nodeTime[node] = time
        #     for nei, neiTime in adj[node]:
        #         dfs(nei, time + neiTime)

        # dfs(k,0)
        # res = max(nodeTime.values())
        # return res if res < float("inf") else -1