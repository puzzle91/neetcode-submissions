class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res =[]
        def check_order(chars):
            stack = []
            
            for char in chars:
                if char == "(":
                    stack.append(char)
                else:
                    # No opening parenthesis available to close.
                    if not stack:
                        return False
                    stack.pop()

            # No unmatched openings should remain.
            print(stack, not stack, 'for initial path:', "".join(chars))
            return not stack

        def backtrack(path,opened, closed):
            if len(path[:]) == 2 * n:
                if check_order(path):
                    res.append("".join(path))
                return
             
            open_par, close_par = "(", ")"

            if opened < n:
                path.append(open_par)
                backtrack(path, opened + 1, closed)
                path.pop()
            if closed < opened:
                path.append(close_par)
                backtrack(path, opened , closed + 1)
                path.pop()

        backtrack([], 0, 0)
     
        return res