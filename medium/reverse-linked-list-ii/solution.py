# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """ Keep inserting node at current position to position m """
        dummy_head = ListNode(0)
        dummy_head.next = head
        insert_p = dummy_head
        tail = head
        counter = 1
        while counter < m:
            insert_p = insert_p.next
            tail = tail.next
            counter += 1
            
        while counter < n:
            target = tail.next
            tail.next = target.next
            target.next = insert_p.next
            insert_p.next = target
            counter += 1
        
        return dummy_head.next