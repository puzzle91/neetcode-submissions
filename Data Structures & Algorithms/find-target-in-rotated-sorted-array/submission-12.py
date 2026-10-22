class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) -1 

        while left <= right:

            midIdx = left + (right - left)//2

            mid = nums[midIdx]

            print("middle number", mid,  "left", nums[left], "right", nums[right] )

            if nums[left] < target:
                left += 1
            elif nums[right] > target:
                right-=1
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                if mid > target:
                    left = midIdx + 1
                elif mid < target:
                    right = midIdx - 1
                
                elif mid == target:
                    return midIdx
        return -1