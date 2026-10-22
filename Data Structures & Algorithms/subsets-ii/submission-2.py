class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        mem_cache = {}
        res = []
        nums.sort()
        def backtrack(start, path, seen = [False] * len(nums)):
           
           
            mem_cache[tuple(path[:])] = True
            res.append(path[:])
        
                 
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                seen[i] = True
                
                backtrack(i + 1, path, seen)
                seen[i] = False
                
                path.pop()
        backtrack(0, [])
       
        return res