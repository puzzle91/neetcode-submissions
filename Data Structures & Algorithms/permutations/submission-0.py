class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                
                n = nums[i]
                if n in path:
                    continue
               
                path.append(n)
                backtrack( path)
                path.pop()
        backtrack( [])
        return res