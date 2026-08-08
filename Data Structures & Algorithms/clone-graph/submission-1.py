"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        nodeMapper = {}
        queue = deque()
        queue.append(node)

        while queue:
            pNode = queue.popleft()

            if pNode not in nodeMapper:
                newNode = Node(pNode.val)
                nodeMapper[pNode] = newNode

            for nei in pNode.neighbors:
                if nei not in nodeMapper:
                    newNode = Node(nei.val)
                    nodeMapper[nei] = newNode
                    nodeMapper[pNode].neighbors.append(newNode)
                    queue.append(nei)
                else:
                    nodeMapper[pNode].neighbors.append(nodeMapper[nei])

        return nodeMapper[node]
        