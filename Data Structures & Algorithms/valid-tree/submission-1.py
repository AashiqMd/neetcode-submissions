class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # All nodes need to be connected (no disjoint) and no cycles
        # 1. Build adjacency list
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        # 2. Created a visited set. It will track all the visited nodes
        visited = set()

        # 3. Define dfs. It will go through all the nodes and return False if it detects a cycle
        # Since it is undirected, we use prev so that it does not go back to the calling node. 
        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                # Return False if there is a loop when you parse this neighbor, but not true until all the neighbors are true
                if not dfs(j,i):
                    return False
            return True
        
        return dfs(0,-1) and len(visited) == n
