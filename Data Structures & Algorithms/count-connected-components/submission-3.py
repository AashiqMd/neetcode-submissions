class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        
        for edge in edges:
            a,b = edge[0], edge[1]
            if parent[a] != parent[b]:
                n-=1
                temp = parent[b]
                for i in range(len(parent)):
                    if parent[i] == temp:
                        parent[i] = parent[a]

        # print(parent)
        return n


        # for edge in edges:
        #     a,b = edge[0], edge[1]
        #     # If at least one of the 2 is getting touched for the 1st time, n-=1
        #     if not (a in touched and b in touched):
        #         n-=1
        #     touched.add(a)
        #     touched.add(b)
        # return n