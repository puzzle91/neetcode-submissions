from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        

        @cache
        def backtrack(start):
            if start >= len(nums):
                return 0 
            tot = 0 
            #option 1 - steal this one and skip next or dont steal this one and go next
            tot = max(nums[start] + backtrack(start+2), backtrack(start+1), tot)

            return tot
        
        a =  max(backtrack(0), backtrack(1))
       
        return a