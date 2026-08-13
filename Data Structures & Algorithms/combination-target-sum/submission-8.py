class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort()
        res = []

        def dfs(i, combination, combSum):
            if combSum == target:
                res.append(combination.copy())
                return
            if i>=len(nums) or combSum > target:
                return
            
            combination.append(nums[i])
            dfs(i, combination, combSum + nums[i])

            combination.pop()
            dfs(i+1, combination, combSum)

            
            # for i in range(start,len(nums)):
            #     if combSum + nums[i] > target:
            #         break
            #     combination.append(nums[i])
            #     dfs(i,combination,combSum + nums[i])
            #     combination.pop()

        dfs(0,[],0)
        return res