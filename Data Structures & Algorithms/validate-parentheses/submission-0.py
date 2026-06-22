class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in "([{":
                stack.append(char)
            else:
                if not stack:
                    return False

                last_open = stack.pop()

                if last_open != pairs[char]:
                    return False

        return len(stack) == 0