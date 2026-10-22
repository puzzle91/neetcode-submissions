class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        min_time = 1
        best_time = max(piles) 

        l, r = min_time, best_time


        def can_eat(eat_rate):
            pile_rate = [(p + eat_rate - 1) // eat_rate for p in piles]
            total_time = sum(pile_rate)
            if all(x>0 for x in pile_rate):
                if total_time <= h:
                    return True
            return False
        while l <=  r:

            mid = l + (r - l)//2
            if can_eat(mid):
                best_time = mid 
                r = mid - 1
            else:
                l = mid + 1 
        
        return best_time