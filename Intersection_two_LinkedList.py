160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB== None:
            return None
        
        A_pointer = headA
        B_pointer = headB
        
        while A_pointer != B_pointer:
            #A_pointer = headB if A_pointer == None else A_pointer.next
            #B_pointer = headA if B_pointer == None else B_pointer.next
            if A_pointer == None:
                A_pointer = headB
            else:
                A_pointer = A_pointer.next
             
            if B_pointer == None:
                B_pointer = headA
            else:
                B_pointer = B_pointer.next
        return A_pointer
