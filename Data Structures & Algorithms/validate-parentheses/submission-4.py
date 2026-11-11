class Solution:
    def isValid(self, s: str) -> bool:
        
        reverse_brack_dict = {')':'(', '}':'{', ']':'['}
        
        stack = []

        for c in s:
            if stack and c in reverse_brack_dict:
                if stack[-1] == reverse_brack_dict[c]:
                        stack.pop()
                else:
                    return False

                 
            else:
                stack.append(c)
        return True if not stack else False
