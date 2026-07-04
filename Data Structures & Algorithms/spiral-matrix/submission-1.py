class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m, n = len(matrix), len(matrix[0])

        top, bottom, left, right = 0, m-1, 0, n-1
        
        while left <=right and top <= bottom:
            # i,j = top,left
            # while j<=right:
            for j in range(left,right+1):
                ans.append(matrix[top][j])
            top+=1

            # while i<=bottom:
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right-=1

            # i,j = bottom,right
            # while j>=left:
            if top <= bottom:
                for j in range(right,left-1,-1):
                    ans.append(matrix[bottom][j])
                bottom-=1

            # while i>=top: 
            if left <= right:
                for i in range(bottom, top-1, -1):
                    ans.append(matrix[i][left])
                left+=1

        return ans

        # Parse the matrix in the following directions until it hits an edge or visited node
        # (0,1), (1,0), (0,-1), (-1,0)
        # directions = [[0,1], [1,0], [0,-1], [-1,0]]

        # i,j= 0,0
        # ans = []
        # n = len(matrix)
        # dirIdx = 0
        # visited = set()

        # for _ in range(n*n):
        #     if i<0 or i>=n or j<0 or j>=n or (i,j) in visited
        #     ans.append(matrix[i][j])
        #     dirIdx = dirIdx % 4
