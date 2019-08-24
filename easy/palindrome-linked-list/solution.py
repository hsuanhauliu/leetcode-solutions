# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """ Reverse second half of the linked list and check.
        
        Time: O(n)
        Space: O(1)
        """
        if not head:
            return True
        
        size = self.get_size(head)
        mid = self.get_center(head, size)
        self.reverse_after(mid)
        curr, mid = head, mid.next
        while mid:
            if curr.val != mid.val:
                return False
            curr, mid = curr.next, mid.next
        return True
        
        
    def get_size(self, head):
        size, curr = 0, head
        while curr:
            size += 1
            curr = curr.next
        return size
            
    def get_center(self, head, size):
        mid = head
        for i in range(1, (size + 1) // 2):
            mid = mid.next
        return mid
    
    def reverse_after(self, head):
        if not head.next or not head.next.next:
            return
        
        curr_p, next_p = head.next, head.next.next
        curr_p.next = None
        while next_p:
            temp = next_p.next
            next_p.next = curr_p
            curr_p, next_p = next_p, temp
        head.next = curr_p