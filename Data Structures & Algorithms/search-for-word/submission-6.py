class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(i,j,idx):
            if (i<0 or j<0 or i>=ROWS or j>=COLS or 
                idx>=len(word) or word[idx] != board[i][j] or
                (i,j) in visited ):
                return False
            if idx == (len(word)-1):
                return True
            visited.add((i,j))
            
            for dr, dc in [(0,1),(0,-1),(-1,0),(1,0)]:
                nr, nc = i+dr, j+dc
                if dfs(nr,nc,idx+1):
                    return True
            
            visited.remove((i,j))

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True
        
        return False



# def traversal(numNodes, graph, executionTimes):
#     adj = defaultdict(list)
#     indegree = [0] * numNodes
#     completedTimes = [0] * numNodes
#     visitedNodes = 0

#     for u,v in graph:
#         adj[u].append(v)
#         indegree[v]+=1
    
#     queue = deque()
#     for i in range(numNodes):
#         if indegree[i] == 0:
#             queue.append(i)
#             completion_times[i] = execution_times[i]

#     while queue:
#         node = queue.popleft()
#         visitedNodes += 1

#         for nei in adj[node]:
#             completedTimes[nei] = max(completedTimes[nei], 
#                                     completedTimes[node] + executionTimes[nei])
#             indegree[nei] -= 1
#             if indegree[nei] == 0:
#                 queue.append(nei)

#     return max(completedTimes) if visitedNodes == numNodes else -1 

