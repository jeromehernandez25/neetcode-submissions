# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # If root is empty, return none
        if root is None:
            return None

        # If root not empty, swap left and right children
        root.left, root.right = root.right, root.left

        # Then recursively call invertTree on left and right children
        self.invertTree(root.left)
        self.invertTree(root.right)

        # After recursion is done, return inverted root
        return root

