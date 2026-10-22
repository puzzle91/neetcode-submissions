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
            return not stack
        def backtrack(path,opened, closed):
            if len(path[:]) == 2 * n:
               
                res.append(path[:])
                return
             
            open_par, close_par = "(", ")"

            if opened < n:
                path.append(open_par)
                backtrack(path, opened + 1, closed)
                path.pop()
            if closed < n:
                path.append(close_par)
                backtrack(path, opened , closed + 1)
                path.pop()

        backtrack([], 0, 0)
        print(res)
        ans = ["".join(x) for x in res if check_order(x)]
        return ans