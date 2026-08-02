class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def dfs(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in seen:
                    perm.append(nums[i])
                    seen.add(nums[i])

                    dfs(perm)

                    perm.pop()
                    seen.remove(nums[i])

        dfs([])
        return res

        