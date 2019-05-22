class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operation(op, a, b):
            if op == "+":
                return a + b
            if op == "-":
                return a - b
            if op == "*":
                return a * b
            return int(a / b)
        
        all_ops = set("+-*/")
        stack = []
        for t in tokens:
            if t in all_ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(operation(t, a, b))
            else:
                stack.append(int(t))
                
        return stack[-1]
