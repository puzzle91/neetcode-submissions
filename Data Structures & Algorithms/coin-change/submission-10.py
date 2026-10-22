from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
       
        coins.sort(reverse=True)
        @cache
        def change_rem(rem):
         
            if rem == 0:
                
                return 0
            coins_used = float('inf')
            for c in coins:
                if rem - c >= 0:
                   
                    coins_used = min(coins_used, 1 + change_rem(rem-c))

            return coins_used
        a = change_rem(amount)
        return -1 if a == float('inf') else a
