# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """ Simply swap the values of the current node and current minimum.

        Time: O(n^2)
        Space: O(1)
        """
        def find_min(node):
            curr_min = curr_i = node
            while curr_i.next:
                curr_i = curr_i.next
                if curr_i.val < curr_min.val:
                    curr_min = curr_i
            return curr_min

        if not head:
            return head

        res = curr_i = head
        while curr_i.next:
            minimum = find_min(curr_i)
            curr_i.val, minimum.val = minimum.val, curr_i.val
            curr_i = curr_i.next

        return res
