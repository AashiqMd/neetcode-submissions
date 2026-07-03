# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        # res is an array of arrays, where each sub-array is the nodes at that depth

        def dfs(root, depth):
            if not root:
                return None
            if len(res) == depth:
                # add an empty array for that depth the first time we unlock the depth
                res.append([])
            
            res[depth].append(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        
        dfs(root, 0)
        return res