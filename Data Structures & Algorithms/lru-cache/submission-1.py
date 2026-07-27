class LL:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.right = None
        self.left = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {}
        
        self.tail = LL()
        self.head = LL()
        self.head.right = self.tail
        self.tail.left = self.head

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self.deleteNode(node)
            self.addNode(node)
            return node.val
        return -1

    def addNode(self, node):
        prev = self.tail.left
        node.right = self.tail
        node.left = prev
        prev.right = node
        self.tail.left = node

    def deleteNode(self, delNode):
        L = delNode.left
        R = delNode.right
        L.right = R
        R.left = L

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.deleteNode(self.hmap[key])
            del self.hmap[key]
        
        Node = LL(key, value)
        self.addNode(Node)
        self.hmap[key] = Node

        if len(self.hmap) > self.capacity:
            lru = self.head.right
            self.deleteNode(lru)
            del self.hmap[lru.key]



