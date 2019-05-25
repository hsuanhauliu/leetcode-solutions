from random import randrange

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList_ms(self, head):
        """ Merge sort implementation
        Time: O(nlogn) in all cases
        Space: O(1) since we're doing it in-place
        """
        if not head:
            return
        
        if not head.next:
            return head
        
        r_head = self.split(head)
        l = self.sortList_ms(head)
        r = self.sortList_ms(r_head)
        return self.merge(l, r)
    
    def split(self, head):
        slow = prev = head
        fast = head.next
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
                
        prev.next = None
        return slow
    
    def merge(self, l, r):
        head = p = ListNode(0)
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        
        p.next = l if l else r
        return head.next


    def sortList_qs(self, head):
        """ Quicksort implementation
        Time: O(nlogn) for average case, but O(n^2) for worst case, which
              can happen a lot if the list is partially or entirely sorted.
        Space: O(1) because we're sorting in-place.
        """
        if not head:
            return

        l_head, r_head = self.partition(head, head.next)
        l_head = self.sortList_qs(l_head)
        r_head = self.sortList_qs(r_head)
        return self.append1(l_head, r_head, head)

    def partition(self, p, h):
        l_head = l_tail = ListNode(0)
        r_head = r_tail = ListNode(0)
        while h:
            if h.val < p.val:
                l_tail.next = h
                l_tail = l_tail.next
            else:
                r_tail.next = h
                r_tail = r_tail.next
            h = h.next

        l_tail.next = None
        r_tail.next = None
        return l_head.next, r_head.next

    def append1(self, l, r, p):
        if not l:
            p.next = r
            return p

        tail = l
        while tail.next:
            tail = tail.next
        tail.next = p
        p.next = r
        return l


    def sortList_qs_random_pivot(self, head):
        """ Normal quick sort with randomized pivot """
        if not head:
            return

        pivot, head = self.random_pick_pivot(head)
        l_head, r_head = self.partition(pivot, head)
        l_head = self.sortList_qs_random_pivot(l_head)
        r_head = self.sortList_qs_random_pivot(r_head)
        return self.append1(l_head, r_head, pivot)

    def random_pick_pivot(self, head):
        count = 0
        p_traverse = head
        while p_traverse:
            count += 1
            p_traverse = p_traverse.next

        index = randrange(count)
        count = 0
        prev = None
        curr = head
        while count < index:
            prev = curr
            curr = curr.next
            count += 1

        if prev:
            prev.next = curr.next
            return curr, head

        return curr, head.next


    def sortList_qs_tail_pointer(self, head):
        """ Quick sort implementation using tail pointer"""
        return self.quicksort_tail_pointer(head)[0]

    def quicksort_tail_pointer(self, head):
        if not head:
            return None, None

        l_head, r_head = self.partition(head, head.next)
        l_head, l_tail = self.quicksort_tail_pointer(l_head)
        r_head, r_tail = self.quicksort_tail_pointer(r_head)
        return self.append2(l_head, l_tail, r_head, r_tail, head)

    def append2(self, l_head, l_tail, r_head, r_tail, p):
        if not l_tail:
            if r_tail:
                p.next = r_head
                return p, r_tail
            return p, p

        l_tail.next = p
        p.next = r_head
        if not r_tail:
            r_tail = p
        return l_head, r_tail


    def sortList_qs_tail_pointer_random_pivot(self, head):
        return self.quicksort_tail_pointer_random_pivot(head)[0]

    def quicksort_tail_pointer_random_pivot(self, head):
        if not head:
            return None, None

        pivot, head = self.random_pick_pivot(head)
        l_head, r_head = self.partition(pivot, head)
        l_head, l_tail = self.quicksort_tail_pointer_random_pivot(l_head)
        r_head, r_tail = self.quicksort_tail_pointer_random_pivot(r_head)
        return self.append2(l_head, l_tail, r_head, r_tail, pivot)


# Test run time of each function
import time

def read(filename):
    """ Read input file """
    l = open(filename, 'r')
    return [int(n) for n in l.read().split(',')]


def build(l):
    """ Build LinkedList from list of int """
    head = p = ListNode(0)
    for n in l:
        p.next = ListNode(n)
        p = p.next

    return head.next


sol = Solution()
l = read("input.txt")
funcs = [sol.sortList_ms,
         sol.sortList_qs,
         sol.sortList_qs_random_pivot,
         sol.sortList_qs_tail_pointer,
         sol.sortList_qs_tail_pointer_random_pivot]

for func in funcs:
    r = build(l)
    start = time.time()
    func(r)
    stop = time.time()
    print("Time:", stop - start)
