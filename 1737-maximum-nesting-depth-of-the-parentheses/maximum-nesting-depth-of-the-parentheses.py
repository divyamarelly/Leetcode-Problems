class Solution:
    def maxDepth(self, s: str) -> int:
        maxdepth = 0
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
                maxdepth = max(maxdepth, len(stack))
            elif c == ')':
                stack.pop()
        return maxdepth