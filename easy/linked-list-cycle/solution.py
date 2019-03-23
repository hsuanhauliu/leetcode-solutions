# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        tortoise = head
        hare = head

        while hare.next and hare.next.next:
            tortoise = tortoise.next
            hare = hare.next.next

            if tortoise == hare:
                return True
        return False
