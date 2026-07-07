class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i : [] for i in range(numCourses)}
        visited = set()

        for pre in prerequisites:
            a,b = pre[0], pre[1]
            adj[a].append(b)
        
        def dfs(node):
            if node in visited:
                return False
            
            visited.add(node)
            for n in adj[node]:
                if not dfs(n):
                    return False
            visited.remove(node)
            adj[node] = []
            return True
        
        for node in range(numCourses):
            if not dfs(node):
                return False
    
        return True
    