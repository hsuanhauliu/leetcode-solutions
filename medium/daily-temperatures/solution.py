class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
	""" Stack solution
	Time: O(n)
	Space: O(n)
	"""
        size = len(t)
        res = [0] * size
        stack = []
        for i in reversed(range(size)):
            temp = t[i]
            while stack and stack[-1][0] <= temp:
                stack.pop()
            
            if stack:
                res[i] = stack[-1][1] - i
            stack.append((temp, i))
        return res