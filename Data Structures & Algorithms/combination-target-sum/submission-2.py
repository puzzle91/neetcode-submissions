class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        mem_cache = {}
        def backtrack(idx, path, total):
            if total == 0:
                res.append(path[:])
                return
            if total in mem_cache:
                return 
           
            for i in range(idx, len(nums)):
               
                if total - nums[i] < 0:
                    continue
                path.append( nums[i])
                backtrack(i, path, total - nums[i])
                path.pop()
        backtrack(0, [], target)
        return res