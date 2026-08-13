class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        seen = set()

        def dfs(perm):
            if len(perm) == len(nums):
                res.add(tuple(perm))
                return
            
            for i in range(len(nums)):
                if i not in seen:
                    perm.append(nums[i])
                    seen.add(i)

                    dfs(perm)

                    perm.pop()
                    seen.remove(i)

        dfs([])
        return list(res)
