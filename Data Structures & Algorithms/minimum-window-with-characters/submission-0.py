class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = defaultdict(int)
        for c in t:
            counts[c]+=1

        l = 0
        # need will be fixed and have will be variable
        need, have = len(counts),0
        shortestSubstring = ""
        minLen = float("inf")

        for r in range(len(s)):
            if s[r] in counts:
                counts[s[r]]-=1
                if counts[s[r]] == 0:
                    have += 1
                
                while have == need:
                    if s[l] in counts:
                        counts[s[l]]+=1
                        if counts[s[l]] == 1:
                            have -= 1
                        if r-l+1 < minLen:
                            minLen = r-l+1
                            shortestSubstring = s[l:r+1]
                    l+=1
        return shortestSubstring