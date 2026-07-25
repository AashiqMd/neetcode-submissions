# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxDiameter = 0
        def maxDepthOfTree(root):
            if not root:
                return 0
            
            return 1 + max(maxDepthOfTree(root.left),maxDepthOfTree(root.right))
        
        maxDiameter = max(maxDiameter, maxDepthOfTree(root.left) + maxDepthOfTree(root.right))
        return max(maxDiameter, self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left))
