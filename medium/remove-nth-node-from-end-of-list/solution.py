# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = fast = dummy = ListNode(0)
        dummy.next = head
        for _ in range(n + 1):
            fast = fast.next
        
        while fast:
            slow, fast = slow.next, fast.next
        
        slow.next = slow.next.next
        return dummy.next