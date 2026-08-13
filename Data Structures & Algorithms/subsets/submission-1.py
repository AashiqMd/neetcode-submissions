class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, subset):
            if i>=len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1, subset)

            subset.pop()
            dfs(i+1, subset)
                
        dfs(0,[])
        return res


        '''
        There are 2 way to do this
        [1,2,3]
        [] comes first
        [1] and rest  ->  [1,2] and rest. -> [1,2,3]
                                             [1,2]
                          [1] and rest.   -> [1,3]
                                             [1]
        [2] and rest  ->  [2,3] and rest. -> [2,3]
                          [2]                [2]
        [3] and rest  ->  End                [3]
        '''