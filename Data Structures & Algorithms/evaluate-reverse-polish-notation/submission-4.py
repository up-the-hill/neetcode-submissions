class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token in symbols:
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                if token == "-":
                    stack.append(a - b)
                if token == "*":
                    stack.append(a * b)
                if token == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]
            
