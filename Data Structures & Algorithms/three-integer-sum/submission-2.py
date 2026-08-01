class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0] > 0:
            return []
        res = []

        # Keep k as the fixed element
        k = 0

        while k < len(nums)-2:
            i,j = k+1, len(nums)-1
            if nums[k] > 0:
                break
            if k > 0 and nums[k] == nums[k-1]:
                k+=1
                continue

            while i < j:
                if nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[k], nums[i], nums[j]])
                    i+=1
                    j-=1
                    while nums[i] == nums[i-1] and i<j:
                        i+=1
                elif nums[i] + nums[j] + nums[k] < 0:
                    i+=1
                else:
                    j-=1
            k+=1

        return res

