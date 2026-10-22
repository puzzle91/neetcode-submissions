import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq.heapify_max(nums)
        cnt = 0

        while len(nums) > 0:
            v1 = heapq.heappop_max(nums)
            cnt+=1
            if cnt == k:
                return v1
            
        return v1