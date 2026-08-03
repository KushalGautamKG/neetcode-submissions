class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        oTc = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in oTc:
                if stack and stack[-1] == oTc[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack