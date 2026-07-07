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
            return None

        clone = {}
        clone[node] = Node(node.val)
        stk = [node]

        while stk:
            originalNode = stk.pop()
            for neighbour in originalNode.neighbors:
                if neighbour in clone:
                    clone[originalNode].neighbors.append(clone[neighbour])
                else:
                    stk.append(neighbour)
                    cloneNeighbour = Node(neighbour.val)
                    clone[originalNode].neighbors.append(cloneNeighbour)
                    clone[neighbour] = cloneNeighbour

        return clone[node]