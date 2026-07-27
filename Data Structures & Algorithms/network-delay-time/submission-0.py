class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build adj list
        adjList = defaultdict(list)
        for u, v, t in times:
            adjList[u].append((v,t))
        
        def dfs(node, time):
            if minTime[node] <= time:
                return 

            minTime[node] = time
            for nei, neiTime in adjList[node]:
                dfs(nei, time + neiTime)

        minTime = {node: float("inf") for node in range(1,n+1)}
        dfs(k, 0)

        # Could not reach all nodes
        if max(minTime.values()) == float("inf"):
            return -1
        return max(minTime.values())