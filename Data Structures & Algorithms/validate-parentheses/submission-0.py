class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_dict = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in paren_dict.values():
                stack.append(c)
            if c in paren_dict.keys():
                if len(stack) > 0 and stack[-1] == paren_dict[c]:
                    stack.pop()
                else:
                    return False
        print(stack)
        return len(stack) == 0

