# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        
        # Depth is also the index in res
        def dfs(root, depth):
            # Base case
            # if no root, return
            if not root:
                return
            if len(res) < depth+1:
                res.append([])

            # Logic
            # Append val into the array for the corresponding level / depth
            res[depth].append(root.val)
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        
        dfs(root, 0)
        return res