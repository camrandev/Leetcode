# Definition for a binary tree node.


#starting at the root node
#set depth to 0

#as long as one node exists, increment depth
#return depth + the greater of a recursive call on left and recursive call on right
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        depth = 1

        depth_right = 0
        depth_left = 0

        if root.right:
            depth_right = self.maxDepth(root.right)
        
        if root.left:
            depth_left = self.maxDepth(root.left)



        return depth + max(depth_right, depth_left)
        