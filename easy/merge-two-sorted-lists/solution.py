# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l_1, l_2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = curr = ListNode(0)
        while l_1 and l_2:
            if l_1.val < l_2.val:
                curr.next = l_1
                l_1 = l_1.next
            else:
                curr.next = l_2
                l_2 = l_2.next
            curr = curr.next

        if l_1:
            curr.next = l_1
        else:
            curr.next = l_2
        return res.next
        