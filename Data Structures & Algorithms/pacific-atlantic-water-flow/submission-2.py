class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        PAC, ATL = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(i,j,prevWater, waterSet):
            # if not( (0<=i<ROWS) and (0<=j<COLS) and 
            #         (heights[i][j] >= prevWater) and 
            #         ((i,j) not in waterSet)):
            #     return
            if (i<0 or j<0 or i>=ROWS or j>=COLS or 
                heights[i][j]<prevWater or
                (i,j) in waterSet):
                return

            waterSet.add((i,j))
            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = i+dr, j+dc
                dfs(nr,nc,heights[i][j],waterSet)


        for i in range(ROWS):
            dfs(i,0,0,PAC)
            dfs(i,COLS-1,0,ATL)

        for j in range(COLS):
            dfs(0,j,0,PAC)
            dfs(ROWS-1,j,0,ATL)
        
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in PAC and (i,j) in ATL:
                    res.append([i,j])

        return res