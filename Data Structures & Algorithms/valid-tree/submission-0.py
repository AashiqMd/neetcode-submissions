class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # All nodes need to be connected (no disjoint) and no cycles

        adj = {i:[] for i in range(n)}

        for p1, p2 in edges:
            adj[p1].append(p2)
            adj[p2].append(p1)
        
        visited = set()
        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)
            for neighbor in adj[i]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, i):
                    return False
            return True

        return dfs(0,-1) and n == len(visited)