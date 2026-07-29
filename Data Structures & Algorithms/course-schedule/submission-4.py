class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahn's algorithm
        indegree = [0] * numCourses
        adj = defaultdict(list)

        for a,b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        finished = 0
        while q:
            node = q.popleft()
            finished += 1
            for nei in adj[node]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return finished == numCourses
        
        # adj = defaultdict(list)
        # visited = set()

        # for a,b in prerequisites:
        #     adj[b].append(a)
        
        # def dfs(node):
        #     if node in visited:
        #         return False
        #     visited.add(node)
        #     for nei in adj[node]:
        #         if not dfs(nei):
        #             return False
        #     visited.remove(node)
        #     # We run the dfs on every node. See loop outside the dfs. 
        #     # If a path is already calculated as no cycles. We don't want to recalculate. 
        #     adj[node] = []
        #     return True

        # for node in range(numCourses):
        #     if not dfs(node):
        #         return False
        # return True
