class Solution(object):
    def diffWaysToCompute(self, input):
        """ Divide and conquer
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        
        res = []
        for i, char in enumerate(input):
            if char in "+-*":
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        res.append(self.calculate(l, r, char))
        return res
    
    def calculate(self, num1, num2, op):
        if op == "+":
            return num1 + num2
        if op == "-":
            return num1 - num2
        return num1 * num2