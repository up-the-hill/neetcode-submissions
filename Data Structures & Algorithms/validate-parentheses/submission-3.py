class Solution:
    def isValid(self, s: str) -> bool:
        # define a dict to find appropriate matching parentheses
        paren_dict = {
            "}": "{",
            ")": "(",
            "]": "["
            }
        # keep a stack of open parens
        stack = []
        for c in s:
            # on a close paren, check if it matches the top of the stack
            if c in paren_dict:
                if stack and stack[-1] == paren_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return False if stack else True


        