# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Global max_diameter to be calculated by dfs
        self.max_diameter = 0

        # DFS function to explore each node in the tree
        def dfs(root):
            # If "root" is none return 0
            if root is None:
                return 0
            
            # Get length of this current "root"
            left = dfs(root.left)
            right = dfs(root.right)

            # Get diameter of this current "root"
            cur_diameter = left + right

            # Compare current diameter to global best diameter
            self.max_diameter = max(self.max_diameter, cur_diameter)

            # Return height of this node to the parent
            return 1 + max(left, right)

        # Call dfs to recursively find the greatest diameter within the root tree
        dfs(root)

        # Return maximum diameter found from dfs
        return self.max_diameter