Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
            
        if l1.val <= l2.val:
            head = l1 
            head.next = self.mergeTwoLists(l1.next, l2)
        else:
            head = l2
            head.next = self.mergeTwoLists(l1, l2.next)
        
        return head 

         
        
        # iteratively
        def mergeTwoLists2(self, l1, l2):
            head = tail = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next   
           	
            tail.next = l1 or l2
            return head.next    
                
