class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       

      
        # Base cases
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        longest = 0
        # Convert to set for O(1) lookup
        num_set = set(nums)

        for num in nums:
            
            
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1

                longest = max(longest, current_length)
                print(f"{longest = }")
            
        

       
        return longest  