class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = Counter()
        for word in words:
            freq += Counter(word)
        
        for f in freq.values():
            if f%len(words) != 0:
                return False
        return True