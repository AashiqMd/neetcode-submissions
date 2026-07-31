class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        count = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                if grid[i][j] == 1:
                    count+=1
                    
        tm = 0
        while queue:
            row, col, time = queue.popleft()
            tm = max(tm, time)
            drs = [(0,1),(0,-1),(-1,0),(1,0)]
            for dr, dc in drs:
                nr, nc = row + dr, col + dc
                if (0<= nr < ROWS) and (0<= nc < COLS) and (grid[nr][nc] == 1):
                    queue.append((nr,nc,time+1))
                    grid[nr][nc] = 2
                    count-=1
                    # print(nr,nc, count)
        
        return tm if count ==0 else -1
