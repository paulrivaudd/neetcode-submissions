class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['#']
        d = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in d:
                if stack.pop() != d[c]:
                    return False
            else:
                stack.append(c)

        return stack == ['#']