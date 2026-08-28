# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # create a dictionary
        # Iterate through each head until null
        # At each head, check and get the node value
        # If value already exists in dictionary return index
        # If loop ends, then no cycle

        # Create a set to remember object identities of each traversed node
        seen = set()
        index = -1
        curNode = head

        # Iterate through each head until null node is reached
        while curNode:
            # If current node already traversed, return true
            if curNode in seen:
                index = curNode.val
                return True
            # If not traversed, add to traversed set list, go next node
            else:
                seen.add(curNode)
                curNode = curNode.next
        
        # No cycle detected in linked list
        return False