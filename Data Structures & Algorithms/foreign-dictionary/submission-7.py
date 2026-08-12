class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        if len(words) == 1:
            return words[0]

        adj = defaultdict(list)
        indegree = {}
        uniqueChars = set()
        topoOrder = ""

        for word in words:
            for char in word:
                indegree[char] = 0
                uniqueChars.add(char)

        for i in range(1,len(words)):
            w1, w2 = words[i-1], words[i]

            j = 0
            minLen = min(len(w1),len(w2))
            while j < minLen:
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    indegree[w1[j]] = indegree.get(w1[j],0)
                    indegree[w2[j]] = indegree.get(w2[j],0) + 1
                    break
                j+=1
            
            if j == minLen and len(w1) > len(w2):
                return ""

        queue = deque()
        for k,v in indegree.items():
            if v == 0:
                queue.append(k)

        while queue:
            node = queue.popleft()
            topoOrder += node
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        return topoOrder if len(topoOrder) == len(uniqueChars) else ""
