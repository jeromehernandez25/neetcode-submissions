# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: # if node has no value
            return None # end recursion

        curr = head # save current node to curr
        if curr.next: # if current node links to another node
            curr = self.reverseList(curr.next) # recurse to the end node in list
            head.next.next = head # point the next node's pointer back to this node
        
        head.next = None # break old link
    
        return curr # return new head/old tail back up the chain