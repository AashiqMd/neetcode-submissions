class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        # These are visited sets for water from each ocean
        pac, atl = set(), set()
        
        def dfs(i,j,visited, prevHeight):
            if (((i,j) in visited) or
                i<0 or j<0 or i>=m or j>=n or
                heights[i][j]<prevHeight):
                return
            
            visited.add((i,j))
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            for dx,dy in directions:
                dfs(i+dx, j+dy, visited, heights[i][j])


        # Setting the prev height to 0, since water is 0 at the sea level and can go to any other height
        for i in range(m):
            dfs(i,0,pac,0)
            dfs(i,n-1,atl,0)

        for j in range(n):
            dfs(0,j,pac,0)
            dfs(m-1,j,atl,0)
        
        res = []
        for i in range(m):
            for j in range(n):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        
        return res