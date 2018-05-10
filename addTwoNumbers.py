# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pointer = l1
        counter = 0
        num1 = 0

        while pointer != None:
            num1 += pow(10, counter) * pointer.val
            pointer = pointer.next
            counter += 1

        pointer = l2
        counter = 0
        num2 = 0

        while pointer != None:
            num2 += pow(10, counter) * pointer.val
            pointer = pointer.next
            counter += 1

        sumOfTwo = num1 + num2
        returnNumber = ListNode(sumOfTwo % 10)
        pointer = returnNumber
        sumOfTwo /= 10
        
        while sumOfTwo != 0:
            pointer.next = ListNode(sumOfTwo % 10)
            pointer = pointer.next
            sumOfTwo /= 10
            
        return returnNumber
                                    
