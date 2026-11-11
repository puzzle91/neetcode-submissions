class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
     
        cars = [(x,y) for (x,y) in zip(position,speed)]
   
        cars.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for c in cars:
            p,s = c
            mv = (target - p) / s 
            stack.append(mv)
            #print(mv)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)