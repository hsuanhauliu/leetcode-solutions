class Solution:
    def generateParenthesis(self, n):
        parentheses = []
        self.build_parentheses_recursive(parentheses, '', n, 0)
        return parentheses

    def build_parentheses_recursive(self, all_parentheses, curr_str, left, right):
        if left == 0 and right == 0:
            all_parentheses.append(curr_str)
            return

        if left > 0:
            self.build_parentheses_recursive(all_parentheses, curr_str + '(', left - 1, right + 1)
        if right > 0:
            self.build_parentheses_recursive(all_parentheses, curr_str + ')', left, right - 1)
