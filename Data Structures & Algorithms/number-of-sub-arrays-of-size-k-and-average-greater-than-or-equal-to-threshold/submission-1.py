class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        l = 0
        cnt = 0 
        curr_total = arr[0]
        # The first element is already a complete window when k == 1.
        if k == 1 and curr_total >= threshold:
            cnt += 1

        for right in range(1, len(arr)):
            curr_total += arr[right]
        
            # Remove the leftmost element if the window exceeds k.
            if right - l + 1 > k:
                curr_total -= arr[l]
                l += 1
                
            if right - l + 1 == k and curr_total/(right-l+1) >= threshold:
                cnt += 1
            
        return cnt