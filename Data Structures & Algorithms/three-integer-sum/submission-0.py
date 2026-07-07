class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        # [-4,-1,-1 0,1,2]
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i!=0 and nums[i] == nums[i-1]:
                continue
            
            l,r = i+1, len(nums)-1
            while l<r:
                total = nums[l] + nums[r] + nums[i]
                if total == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1
                elif total < 0:
                    l+=1
                elif total > 0:
                    r-=1
        return ans
