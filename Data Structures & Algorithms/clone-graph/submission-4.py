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
        nodeMapper[node] = Node(node.val)

        while queue:
            pNode = queue.popleft()
            pNodeClone = nodeMapper[pNode]

            for nei in pNode.neighbors:
                if nei not in nodeMapper:
                    newNode = Node(nei.val)
                    nodeMapper[nei] = newNode
                    pNodeClone.neighbors.append(newNode)
                    queue.append(nei)
                else:
                    pNodeClone.neighbors.append(nodeMapper[nei])

        return nodeMapper[node]
        