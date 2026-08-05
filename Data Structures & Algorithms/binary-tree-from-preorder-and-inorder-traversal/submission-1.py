# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        root = preorder[0]
        pivotIdx = inorder.index(root)
        leftLen = pivotIdx
        
        rootNode = TreeNode(root)
        rootNode.left = self.buildTree(preorder[1:1+leftLen] , inorder[:pivotIdx])
        rootNode.right = self.buildTree(preorder[1+leftLen:] , inorder[pivotIdx+1:])

        return rootNode