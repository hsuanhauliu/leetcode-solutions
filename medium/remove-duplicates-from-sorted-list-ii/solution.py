# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        
        dummy_head = ListNode(0)
        dummy_head.next = head
        prev = dummy_head
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                skip = curr.next
                while skip and skip.val == curr.val:
                    skip = skip.next
                prev.next = curr = skip
            else:
                prev = curr
                curr = curr.next
        
        return dummy_head.next