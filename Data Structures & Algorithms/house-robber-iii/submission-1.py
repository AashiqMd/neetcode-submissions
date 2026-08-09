# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # memo = {}

        def dfs(root):
            if not root:
                return (0,0) #(include, exclude)

            left, right = dfs(root.left), dfs(root.right)
            include = root.val + left[1] + right[1]
            exclude = max(left) + max(right)

            return (include, exclude)
        
        return max(dfs(root))