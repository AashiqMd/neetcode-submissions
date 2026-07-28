class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = -1
        n = len(nums)

        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break
        
        if index == -1:
            nums.reverse()
            return
        
        for i in range(n-1,-1,-1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break
                
        l,r = index + 1, n-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1