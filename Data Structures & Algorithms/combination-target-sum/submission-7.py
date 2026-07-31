class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(start, combination, combSum):
            if combSum == target:
                res.append(combination.copy())
                return
            # if combSum > target:
            #     return
            
            for i in range(start,len(nums)):
                if combSum + nums[i] > target:
                    break
                combination.append(nums[i])
                dfs(i,combination,combSum + nums[i])
                combination.pop()

        dfs(0,[],0)
        return res