class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        rank = [0] * n
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        
        for x,y in edges:
            px, py = find(x), find(y)
            if rank[px] > rank[py]:
                parents[py] = px
            elif rank[px] < rank[py]:
                parents[px] = py
            else:
                parents[py] = px
                rank[px]+=1
            
        components = 0
        for i in range(n):
            if find(i) == i:
                components+=1
        return components
        
        # parent = [i for i in range(n)]
        
        # for edge in edges:
        #     a,b = edge[0], edge[1]
        #     if parent[a] != parent[b]:
        #         n-=1
        #         temp = parent[b]
        #         for i in range(len(parent)):
        #             if parent[i] == temp:
        #                 parent[i] = parent[a]

        # # print(parent)
        # return n

        # This works but breaks for duplicate edges. 
        # for edge in edges:
        #     a,b = edge[0], edge[1]
        #     # If at least one of the 2 is getting touched for the 1st time, n-=1
        #     if not (a in touched and b in touched):
        #         n-=1
        #     touched.add(a)
        #     touched.add(b)
        # return n