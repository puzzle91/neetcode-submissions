class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        best = r

        while l <= r:
            speed = l + (r - l) // 2
            hours = sum((pile + speed - 1) // speed for pile in piles)

            if hours <= h:
                # This speed works; try a smaller one.
                best = speed
                r = speed - 1
            else:
                # This speed and all slower speeds fail.
                l = speed + 1

        return best