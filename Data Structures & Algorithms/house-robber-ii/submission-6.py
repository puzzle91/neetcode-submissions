from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def solve(houses):
            
            @cache
            def backtrack(start):
                
                if start >= len(houses):
                    return 0

                tot = 0 
                # Option 1 - take this house and remove previous house
                # Option 2 - move onto next house and take previous house
                tot = max(tot, houses[start]  + backtrack(start + 2),  backtrack(start+1) )
                return tot
            return backtrack(0)
        return max(solve(nums[1:]), solve(nums[:-1]))