class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque()
        queue.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        
        while queue:
            word, seqLen = queue.popleft()
            for i in range(len(word)):
                for c in range(97,123):
                    if chr(c) == word[i]:
                        continue
                    newWord = word[:i] + chr(c) + word[i+1:]
                    if newWord == endWord:
                        return seqLen+1
                    if newWord in wordList and newWord not in visited:
                        visited.add(newWord)
                        queue.append((newWord, seqLen+1))

        return 0