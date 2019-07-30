# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """ Straightforward pointer approach.
        
        Time: O(n)
        Space: O(1)
        """
        curr = head
        first = first_tail = ListNode(0)    # dummy head
        second = second_tail = ListNode(0)  # dummy head 2
        
        while curr:
            if curr.val < x:
                first_tail.next = curr
                first_tail = first_tail.next
            else:
                second_tail.next = curr
                second_tail = second_tail.next
            curr = curr.next
        
        first_tail.next = second.next
        second_tail.next = None
        return first.next