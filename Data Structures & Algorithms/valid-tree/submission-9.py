class DSU:
    def __init__(self,n):
        self.parents = [i for i in range(n)]
        self.rank = [0]*n
        self.components = n
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] > self.rank[py]:
            self.parents[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parents[px] = py
        else:
            self.parents[py] = px
            self.rank[px]+=1
        self.components -=1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # dsu = DSU(n)
        # for x,y in edges:
        #     if not dsu.union(x,y):
        #         return False
        # return True if dsu.components == 1 else False

        adj = defaultdict(list)
        # If self loops are allowed. Write a condition where if u==v continue
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        def dfs(parent, node):
            if node in visited:
                return False

            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(node, nei):
                    return False
            return True
        
        if not dfs(-1,0):
            return False
            
        return len(visited) == n

        

        # adj = defaultdict(list)
        # for u,v in edges:
        #     adj[u].append(v)
        #     adj[v].append(u)

        # visited = set()
        # def dfs(node, parent):
        #     if node in visited:
        #         return False
            
        #     visited.add(node)
        #     for nei in adj[node]:
        #         if nei == parent:
        #             continue
        #         if not dfs(nei, node):
        #             return False
            
        #     return True

        # if not dfs(0, -1):
        #     return False
        
        # return True if len(visited) == n else False