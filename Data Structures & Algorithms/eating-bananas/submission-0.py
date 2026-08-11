class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = max(piles)

        while l<=r:
            mid = (l+r)//2
            # Mid is the potential k value

            calc_h = 0
            for i in range(len(piles)):
                calc_h += math.ceil(piles[i]/mid)
            
            if calc_h > h:
                l = mid+1
            else:
                res = min(res, mid)
                r = mid-1

        return res