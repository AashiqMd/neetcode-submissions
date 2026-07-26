class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        res = []
        
        # Concept is to use 1 element as a permutation and then add remainin elements to every spot. 
        perms = self.permute(nums[1:])
        
        for perm in perms:
            for i in range(len(perm)+1):
                permCopy = perm.copy()
                permCopy.insert(i, nums[0])
                res.append(permCopy)
        
        return res