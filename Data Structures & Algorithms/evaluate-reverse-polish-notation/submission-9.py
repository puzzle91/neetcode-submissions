class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        stack = []
        signs_dict = {"+", "-", "*", "/"}
        for t in tokens:
            if t in signs_dict:
                b,a = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    q = abs(a) // abs(b)
                    stack.append(q if a * b >= 0 else -q)
            else:
                stack.append(int(t))
        return stack[-1]