# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        queue = deque([root])
        arr = []

        while queue:
            node = queue.popleft()
            if not node:
                arr.append("null")
                continue
            arr.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        print(arr)
        return ",".join(arr)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        arr = data.split(',')
        root = TreeNode(int(arr[0]))
        queue = deque([root])
        i = 0

        while queue:
            node = queue.popleft()
            i+=1
            if arr[i] == 'null':
                node.left = None
            else:
                node.left = TreeNode(int(arr[i]))
                queue.append(node.left)
            i+=1 
            if arr[i] == 'null':
                node.right = None
            else:    
                node.right = TreeNode(int(arr[i]))
                queue.append(node.right)

        return root

