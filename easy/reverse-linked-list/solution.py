# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        """ Reverse iteratively
        Time: O(n)
        Space: O(1)
        """
        if head:
            prev = head
            tail = head.next
            while tail:
                prev.next = tail.next
                tail.next = head
                head, tail = tail, prev.next
        return head
    
    
    def reverseList2(self, head: ListNode) -> ListNode:
        """ Reverse recursively.
        Time: O(n)
        Space:O(1)
        """
        def reverse(node):
            if not node.next:
                return node, node
            
            head, tail = reverse(node.next)
            tail.next = node
            node.next = None
            return head, node
        
        if head:
            head, _ = reverse(head)
        return head