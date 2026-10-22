class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
      
        


        # two pointer approach
       
        
       
        max_vol = 0
        left = 0
        right = len(heights)  - 1
        
                    
                
        
            
            
        while left <  right:
            l  = right - left
            h = min(heights[right], heights[left])
            
            vol = l * h
            print(f"length {l} ; height {h} ; vol {vol} ; max_vol {max_vol}, left {left} right {right}")

            
            max_vol = max(max_vol,vol)
            
            if heights[left] < heights[right]:
                
                left += 1
            else:
                right-=1
        return max_vol

