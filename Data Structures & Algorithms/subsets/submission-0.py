class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        #nums.sort()
        def backtrack(start, path):
            
            res.append(path[:])

            for i in range(start, len(nums)):
                val = nums[i]
                path.append(val)
                backtrack(i+1, path)
                path.pop()
        backtrack(0, [])
        
        res = sorted(res, key = lambda x: len(x), reverse=True)
        return res