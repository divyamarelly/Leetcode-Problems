class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) != 0 and c.lower() == stack[-1].lower() and (c.islower() and stack[-1].isupper() or c.isupper() and stack[-1].islower()):
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
