from functools import cache
class Solution:
    def totalMoney(self, n: int) -> int:
        
        @cache
        def get_money(day):
            if 0 <= day <= 7:
                
                res = day
                #return mem_cache[day]
            
            else:
                weeks = (day - 1) // 7
                weekday = (day - 1) % 7
                res = weeks + get_money(weekday) + 1
            return res
            
        tot = 0
       
        for _ in range(n+1):
            tot+= get_money(_)
        return tot
        
        