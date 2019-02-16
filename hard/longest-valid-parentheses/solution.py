class Solution(object):
    def longestValidParentheses(self, s: 'str') -> 'int':
        """
        :type s: str
        :rtype: int
        """
        longest_p = 0
        stack = [0]

        for p in s:
            if p == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    last = stack.pop()
                    stack[-1] += last + 2
                    longest_p = max(longest_p, stack[-1])
                else:
                    stack = [0]

        return longest_p
