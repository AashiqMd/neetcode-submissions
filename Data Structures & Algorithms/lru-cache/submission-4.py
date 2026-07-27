class Node:
    def __init__(self,key=0,value=0):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = {}

        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head

    def addNode(self,node):
        L, R = self.tail.prev, self.tail
        L.next, R.prev = node, node
        node.prev, node.next = L, R

    def delNode(self,node):
        L, R = node.prev, node.next
        L.next, R.prev = R, L

    def get(self, key: int) -> int:
        if key in self.hmap:
            node = self.hmap[key]
            self.delNode(node)
            self.addNode(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        newNode = Node(key,value)
        self.addNode(newNode)
        if key in self.hmap:
            dNode = self.hmap[key]
            self.delNode(dNode)
        self.hmap[key] = newNode

        if len(self.hmap) > self.capacity:
            lru = self.head.next
            self.delNode(lru)
            del self.hmap[lru.key]
        
