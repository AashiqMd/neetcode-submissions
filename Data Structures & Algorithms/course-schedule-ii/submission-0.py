class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        topoOrder = []

        for a,b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            topoOrder.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return topoOrder if len(topoOrder) == numCourses else []