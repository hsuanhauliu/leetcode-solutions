class Solution:
    def scoreOfParentheses(self, s):
        stack = []
        curr = 0
        for i in s:
            if i == '(':
                stack.append(curr)
                curr = 0
            else:
                curr += stack.pop() + max(curr, 1)
        return curr