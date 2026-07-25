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
        lDepth = self.maxDepthOfTree(root.left)
        rDepth = self.maxDepthOfTree(root.right)

        # If the longest diameter passes through the root
        maxDiameter = max(maxDiameter, lDepth + rDepth)

        # Account for of the longest diameter is in the left or right subtree
        return max(maxDiameter, self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left))
    
    def maxDepthOfTree(self, root):
        if not root:
            return 0
        
        return 1 + max(self.maxDepthOfTree(root.left), self.maxDepthOfTree(root.right))