class Node:
    def __init__(self):
        self.endsHere = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.dummy = Node()

    def addWord(self, word: str) -> None:
        node = self.dummy
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                newNode = Node()
                node.children[c] = newNode
                node = newNode
        node.endsHere = True

    def search(self, word: str) -> bool:
        node = self.dummy

        def helper(node, wrd):
            if wrd == "":
                return node.endsHere
        
            if wrd[0] in node.children:
                nd = node.children[wrd[0]]
                return helper(nd,wrd[1:])
            elif wrd[0] == ".":
                res = False
                for child in node.children:
                    res = res or helper(node.children[child],wrd[1:])
                return res
            else:
                return False
        
        return helper(node, word)

