"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node

        cloned = {}
        queue = deque([node])
        
        newNode = Node(node.val)
        cloned[node] = newNode

        while queue:
            nd = queue.popleft()

            for nei in nd.neighbors:
                if nei not in cloned:
                    queue.append(nei)
                    newNode = Node(nei.val)
                    cloned[nei] = newNode
                    cloned[nd].neighbors.append(newNode)
                else:
                    cloned[nd].neighbors.append(cloned[nei])
        
        return cloned[node]