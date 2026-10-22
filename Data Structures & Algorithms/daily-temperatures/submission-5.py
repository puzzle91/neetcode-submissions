class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        curr_tmp = max_tmp = 0
        stack = []
        res = [0] * len(temperatures)
        stack.append(curr_tmp)
        
        
      
        for i in range(len(temperatures)):
            prev = stack[-1]
            print(f"prev {prev}, {temperatures[stack[-1]]}")
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                print(f"prev_day {prev_day}")
                res[prev_day] = i - prev_day
                new_temp = temperatures[i]
                
                
                        
                max_tmp = max(max_tmp, new_temp)
            stack.append(i)
             
        return res
                             
                    
