# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Write a function to iterate through the root tree until the subroot node value is found
        # Then write a function to then compare whether the root has the same structure as the subroot

        # Function to iterate through root to find subroot start
        def findSubroot(root, subRoot):
            # If root node value is zero, return -1
            if root is None:
                return -1
            
            # Run checkSame if root value is the same as subroot value
            if root.val == subRoot.val:
                same = checkSame(root, subRoot)
                if same != -1:
                    return same
            
            # If value not the same, check root children for subroot node
            left = findSubroot(root.left, subRoot)
            right = findSubroot(root.right, subRoot)

            # If either left or right children contain subroot, return 0, otherwise -1
            if left == 0 or right == 0:
                return 0
            else:
                return -1


        # Function to check if subroot exists within root
        def checkSame(root, subroot):
            # If either root or subroot have a value where the other does not,
            # then their structure is not the same
            if root is None and subroot:
                return -1
            
            if subroot is None and root:
                return -1
            
            # If both are none, then strucure is same, stop recursing and return 0
            if root is None and subroot is None:
                return 0
            
            # If values differ than tree structure not the same
            if root.val != subroot.val:
                return -1
            
            # If node values the same, then check if children nodes are also the same
            left = checkSame(root.left, subroot.left)
            if left == -1:
                return -1
            
            right = checkSame(root.right, subroot.right)
            if right == -1:
                return -1
            
            # If left and right children structures are the same, return 0
            if left == 0 and right == 0:
                return 0
        
        ans = findSubroot(root, subRoot)
        if ans == -1:
            return False
        else:
            return True


        