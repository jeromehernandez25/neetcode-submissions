# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Write a helper function that iterates through both trees from the root
        # Checking if each one has the same left and right nodes
        # If at any point the trees have difference in their nodes, then return false
        # up the recursive function calls

        def checkSame(root1, root2):
            # If root1 does not have a value and root2 does, return -1
            if root1 is None and root2:
                return -1
            
            # If root2 does not have a value and root1 does, return -1
            if root2 is None and root1:
                return -1

            # If both are None, they are the same structure
            if root1 is None and root2 is None:
                return 0
            
            # If values differ, return -1
            if root1.val != root2.val:
                return -1
            
            # If both root1 and root2 have a value, check their children
            left = checkSame(root1.left, root2.left)
            if left == -1:
                return -1
            
            right = checkSame(root1.right, root2.right)
            if right == -1:
                return -1
            
            # Booth structures are the same if this point is reached
            return 0

        # Run the helper function on the two tree
        ans = checkSame(p, q)

        # Return whether the strucutres are the same or not
        if ans == -1:
            return False
        else:
            return True
            