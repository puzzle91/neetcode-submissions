class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
     
        cars = [(x,y) for (x,y) in zip(position,speed)]
   
        cars.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for c in cars:
            p,s = c
            time = (target - p) / s  # time = (target - starting position)/speed
                                   # time = (distance remaining)/speed
            stack.append(time)
            # if one time that started after is less than one time that started before (cars caught up) then pop for stack
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
             # A car forms a new fleet only if it can't catch the fleet ahead.
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)