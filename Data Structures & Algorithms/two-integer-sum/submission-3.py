class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen_cache = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement not in seen_cache:
                seen_cache[complement] = i 

            if nums[i] in seen_cache:
                    if seen_cache[nums[i]] != i:
                        return [seen_cache[nums[i]], i]

        

