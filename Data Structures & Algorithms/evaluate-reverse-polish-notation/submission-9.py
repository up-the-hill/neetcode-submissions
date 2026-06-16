class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []
        for t in tokens:
            if t in operators:
                if t == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a + b)
                if t == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                if t == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a * b)
                if t == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))
            else:
                stack.append(int(t))

        return stack[0]
        