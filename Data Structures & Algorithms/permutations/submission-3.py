class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def dfs(start,perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            
            for i in range(len(nums)):
                if nums[i] not in visited:
                    perm.append(nums[i])
                    visited.add(nums[i])

                    dfs(i+1,perm)

                    perm.pop()
                    visited.remove(nums[i])

        dfs(0,[])
        return res

        