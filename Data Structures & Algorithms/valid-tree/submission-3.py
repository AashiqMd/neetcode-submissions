class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        self.count = 0
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node, parent):
            if node in visited and node != parent:
                return False
            
            visited.add(node)
            self.count+=1
            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            
            return True

        if not dfs(0, -1):
            return False
        
        return True if self.count == n else False