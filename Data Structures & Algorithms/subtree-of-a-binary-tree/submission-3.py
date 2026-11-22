# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self, rootA: Optional[TreeNode], rootB: Optional[TreeNode]):
        if rootA is None and rootB is None:
            return True
        if rootA is None or rootB is None:
            return False
        
        return (rootA.val == rootB.val) and  self.isSameTree(rootA.left, rootB.left) and self.isSameTree(rootA.right, rootB.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        