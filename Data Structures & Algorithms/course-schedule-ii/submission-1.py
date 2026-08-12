class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = defaultdict(list)
        topoOrder = []

        for a,b in prerequisites:
            if a == b:
                return False
            adj[b].append(a)
            indegree[a]+=1
        
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            topoOrder.append(node)
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    queue.append(nei)

        return topoOrder if len(topoOrder) == numCourses else []