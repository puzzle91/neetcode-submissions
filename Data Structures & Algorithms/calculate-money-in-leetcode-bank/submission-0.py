from functools import cache
class Solution:
    def totalMoney(self, n: int) -> int:
        mem_cache = {}
        
        def get_money(day):
            if 0 <= day <= 7:
                mem_cache[day] = day
                
                #return mem_cache[day]
            
            else:
                weeks = (day - 1) // 7
                weekday = (day - 1) % 7
                mem_cache[day] = weeks + mem_cache[weekday] + 1
            return mem_cache[day]
            
        tot = 0
       
        for _ in range(n+1):
            tot+= get_money(_)
        return tot
        
        