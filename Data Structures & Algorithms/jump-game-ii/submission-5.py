class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = {}
        if len(nums) == 1:
            return 0 
        def dfs(i = 0):

            if i == len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            if nums[i] == 0:
                return float('inf')

            max_jump = max(1, nums[i])
            end = min(len(nums) - 1, i + nums[i])
            res = float('inf')
            for j in range(i+1, end + 1):
                res = min(res, 1 + dfs(j))

                  
            memo[i] = res 
            return memo[i]

        return  dfs(0)