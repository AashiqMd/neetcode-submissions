class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Area = min(lheight, rheight) * (ridx - lidx)
        # You are limited by the smaller height. Move the index of the smaller height

        l,r = 0, len(height)-1
        maxWater = 0

        while l<r:
            maxWater = max(min(height[l], height[r]) * (r - l), maxWater)
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1

        return maxWater