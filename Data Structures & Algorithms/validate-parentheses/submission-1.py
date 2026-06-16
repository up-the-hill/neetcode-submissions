class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_dict = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in paren_dict:
                if len(stack) > 0 and stack[-1] == paren_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0

