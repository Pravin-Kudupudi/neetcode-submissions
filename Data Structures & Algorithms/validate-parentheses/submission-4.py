class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if stack and c in hashMap and stack[-1] == hashMap[c]:
                stack.pop()
            else:
                stack.append(c)
            print(stack)
        
        return not stack
