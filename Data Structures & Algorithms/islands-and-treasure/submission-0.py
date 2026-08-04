class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])

        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i,j,0))
        
        while queue:
            r,c,cnt = queue.popleft()
            if (r<0 or c<0 or r>=m or c>=n or
                grid[r][c] == -1 or grid[r][c]<cnt):
                continue

            grid[r][c] = cnt

            for dr,dc in [(0,1),(0,-1),(-1,0),(1,0)]:
                nr, nc = r+dr, c+dc
                queue.append((nr,nc,cnt+1))
        
        return