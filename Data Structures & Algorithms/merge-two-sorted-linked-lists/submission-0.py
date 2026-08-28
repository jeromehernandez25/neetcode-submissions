# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode() # create linked list to hold combined results
        tail = ans       # tail of list to append results to

        headA = list1   # head of list1
        headB = list2   # head of list2

        while headA and headB:  # iterate until either list is empty
            if headA.val <= headB.val: # point tail to headA if less than B
                tail.next = headA
                headA = headA.next
            else:                   # point tail to headB if less than A
                tail.next = headB
                headB = headB.next
            
            tail = tail.next    # increment tail to next node
        
        if headA: # attach remainder of headA to tail
            tail.next = headA
        elif headB: # attach remaind of headB to tail
            tail.next = headB

        return ans.next # ListNode are initialized with a 0 node, return the list after that