class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Area = min height * length
        l,r = 0, len(heights)-1
        maxVolume = 0
        while l<r:
            volume = min(heights[l],heights[r]) * (r-l)
            maxVolume = max(maxVolume, volume)
            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1
        return maxVolume