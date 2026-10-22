class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        

        stack = []
        signs_dict = {"+", "-", "*", "/"}
        for t in tokens:
            if t in signs_dict:
                b, a = stack.pop(), stack.pop()
                stack.append(a + b if t == "+" else a - b if t == "-" else a * b if t == "*" else int(a / b))
            else:
                stack.append(int(t))
        return stack[-1]