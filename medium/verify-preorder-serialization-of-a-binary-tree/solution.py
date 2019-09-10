class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == '#':
            return True
        
        stack = []
        left = True
        for n in preorder.split(','):
            if n == '#':
                if left:   # left end
                    if stack:
                        stack.append(('#', left))
                        left = False
                    else:
                        return False
                else:   # right end
                    if not stack:
                        return False
                    while not stack[-1][1] or stack[-1][0] == '#':
                        stack.pop()
                        if not stack:
                            return False
                    stack.pop()
            else:
                stack.append((n, left))
                left = True
        return not stack