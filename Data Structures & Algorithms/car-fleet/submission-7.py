class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = [(i, x) for i, x in zip(position, speed)]
        pos_speed = sorted(pos_speed, key=lambda x : x[0], reverse=True)
        stack = []
        for p, s in pos_speed:
            speed = (target - p) / s

            stack.append(speed)
            if len(stack) >=2 and   stack[-1] <= stack[-2]:
                #if new car has speed that is less than previous car
                #they will merge:
                    
                    stack.pop()

             
           
         
        return len(stack)
