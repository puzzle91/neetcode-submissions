from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        
        @cache
        def check_climb(n):
            if n <= 2:
                return n
            return check_climb(n-2) + check_climb(n-1)
        
        return check_climb(n)