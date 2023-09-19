# Definition for a binary tree node.

#starting the top node, take the following actions
    #if both left and right exist, swap them
    
    #call the swap function on each existing node


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        root.right, root.left = root.left, root.right
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root
        