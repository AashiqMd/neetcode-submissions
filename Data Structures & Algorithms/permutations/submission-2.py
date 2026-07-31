class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def dfs(permutation,seen):
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
            
            for num in nums:
                if num in seen:
                    continue
                permutation.append(num)
                seen.add(num)
                
                dfs(permutation, seen)
                
                seen.remove(num)
                permutation.pop()

            
        dfs([],seen)
        return res