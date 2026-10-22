class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #find n rotations - this should give us an indication of where  to start the search
        number_of_rotations = 0

        left, right = 0, len(nums) -1 

        start, end = nums[0], nums[-1]

        print(start,  end, "start and end")

        lowest = float('inf')
        while left <= right:

            midIdx = left + (right - left)//2
            mid = nums[midIdx]
            print("Curr mid", mid)
            lowest = min(lowest, mid)
            if mid >= start and mid >= end:
                left = midIdx+1 
            elif mid <= end and mid <= start:
                right = midIdx - 1
            elif mid >= start and mid <= end:
                right = midIdx-1
            else:
                right = midIdx+1 
            
        return lowest