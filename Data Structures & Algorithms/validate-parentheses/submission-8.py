class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if stack and c in parMap and parMap[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        return not stack
        