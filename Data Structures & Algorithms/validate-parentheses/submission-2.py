class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # FIFO -> First in First Out
        complements = {']':'[', '}':'{', ')':'('}
        for idx, symb in enumerate(s):
             
            print(stack, "stack")
            if symb in complements:
                if stack and stack[-1] == complements[symb]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(symb)
                
             
            
             
            print(stack, 'stack 1')

        print("final stack", stack)
        return False if len(stack) > 0 else True