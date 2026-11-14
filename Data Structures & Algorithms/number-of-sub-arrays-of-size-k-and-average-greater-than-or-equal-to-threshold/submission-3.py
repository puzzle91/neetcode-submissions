class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        l = 0
       
        curr_total = 0
        cnt = 0

        for right in range(len(arr)):
            curr_total += arr[right]
        
            # Remove the leftmost element if the window exceeds k.
            if right - l + 1 > k:
                curr_total -= arr[l]
                l += 1
                
            if right - l + 1 == k and curr_total >= threshold*(right-l+1):
                cnt += 1
            
        return cnt