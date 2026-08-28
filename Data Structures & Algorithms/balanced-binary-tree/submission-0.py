# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to get the height of each subtree
        def getHeight(root):
            if root is None:
                return 0
            
            # Recursively call getHeight on each branch
            # If any branch has is unbalanced, immediately
            # return -1 so that the original call can see
            # that the tree is unbalanced, False
            left = getHeight(root.left)
            if left == -1:
                return -1
            
            right = getHeight(root.right)
            if right == -1:
                return -1

            # If left and right branches are individually balanced
            # Compare to see if their heights differ by no more than 1
            # If they do, return -1, if not return their max height 
            # plus the height of this current node
            if abs(left - right) > 1:
                return -1
            else:
                return 1 + max(left, right)
        
        # Run recursive helper function on root
        ans = getHeight(root)

        # If ans is -1, tree is unbalanced return False
        if ans == -1:
            return False
        # If anse anythign other than -1, return True
        else:
            return True
