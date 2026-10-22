class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        def canEatAll(k):
            """Check if we can eat all bananas at speed k within h hours"""
            total_time = 0
            for pile in piles:
                # Time to eat this pile at speed k
                total_time += math.ceil(pile / k)
            return total_time <= h
        
        # Binary search on eating speed
        left, right = 1, max(piles)
        result = right
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if canEatAll(mid):
                # Can eat at this speed, try slower
                result = mid
                right = mid - 1
            else:
                # Too slow, need faster speed
                left = mid + 1
        
        return result
            