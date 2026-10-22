class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = backward = 1
        output = [1] * len(nums)
        for i in range(len(nums)):
            prefix = nums[i]
            output[i] = forward
            forward  *= prefix
            
        
        for j in range(-1, -1 - len(nums), -1):
            suffix = nums[j]
            output[j] *= backward
            backward *= suffix

      
            
        return output
        