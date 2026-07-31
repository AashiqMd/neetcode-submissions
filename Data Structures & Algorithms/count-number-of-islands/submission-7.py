class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        queue = deque()

        # def dfs(i,j):
        #     if not ((0<=i<ROWS) and (0<=j<COLS) and grid[i][j] == '1'):
        #         return

        #     grid[i][j] = '0'
        #     for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        #         nr, nc = i + dr, j + dc
        #         dfs(nr,nc)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    grid[i][j] = "0"
                    queue.append((i,j))
                    count+=1

                    while queue:
                        row, col = queue.popleft()
                        for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                            nr, nc = row + dr, col + dc
                            if (0<=nr<ROWS) and (0<=nc<COLS) and grid[nr][nc] == '1':
                                grid[nr][nc] = "0"
                                queue.append((nr,nc))
        
        return count