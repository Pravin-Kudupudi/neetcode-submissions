class Solution:
    def isValid(self, s: str) -> bool:
        lookUp = { "}": "{", ")": "(", "]": "["}
        stack = []

        for c in s:
            if c not in lookUp:
                stack.append(c)
            elif stack and lookUp[c] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not stack