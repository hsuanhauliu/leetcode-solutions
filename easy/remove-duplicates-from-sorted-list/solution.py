# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """ Skip any node that has the same value as the previous node """
        if not head:
            return
        
        prev = head
        curr = head.next
        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
                curr = prev.next
            else:
                prev = prev.next
                curr = curr.next
                
        return head
                