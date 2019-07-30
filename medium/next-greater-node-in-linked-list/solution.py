# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        """ Two stacks and two passes. Get all numbers first, then
        use another stack to keep track of numbers greater than
        each previous element.
        
        Time: O(n)
        Space: O(n)
        """
        curr = head
        num_stack = []
        while curr:
            num_stack.append(curr.val)
            curr = curr.next
        
        size = len(num_stack)
        res = [0] * size
        large_stack = []
        for i in reversed(range(size)):
            curr_num = num_stack.pop()
            if large_stack:
                while large_stack and not res[i]:
                    next_num = large_stack[-1]
                    if next_num <= curr_num:
                        large_stack.pop()
                    else:
                        res[i] = next_num
            large_stack.append(curr_num)
                
        return res