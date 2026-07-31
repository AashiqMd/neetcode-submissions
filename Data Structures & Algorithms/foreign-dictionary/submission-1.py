class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(list)
        indegree = {}
        uniqueChars = set()

        for word in words:
            for c in word:
                if c not in indegree:
                    indegree[c] = 0
                    uniqueChars.add(c)

        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            idx = min(len(w1),len(w2))
            for j in range(idx):
                if w1[j] == w2[j]:
                    continue
                adj[w1[j]].append(w2[j])
                indegree[w2[j]] += 1
                break
            if w1[:idx] == w2[:idx] and len(w1) > len(w2):
                return ""

        # print(adj)
        # print(indegree)

        queue = deque()
        for k,v in indegree.items():
            if v == 0:
                queue.append(k)
        
        res = ""
        while queue:
            node = queue.popleft()
            res += node
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        return res if len(res) == len(uniqueChars) else ""
