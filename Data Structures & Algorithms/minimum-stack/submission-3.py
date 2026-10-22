class MinStack:
    from typing import Union
    from collections import deque
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.top_element: Union[int , None] = None
        

    def push(self, val: int) -> None:
        
      
      
        self.stack.append(val)

        # Push to min_stack if it's empty or the new value is smaller or equal
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

           

        

    def pop(self) -> None:
        
        if self.stack:
             
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
             


   

    def top(self) -> int:
         
        return self.stack[-1] if self.stack else None

        

    def getMin(self) -> int:
       
        return self.min_stack[-1] if self.min_stack else None
         
        
