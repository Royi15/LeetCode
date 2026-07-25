# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def height(self, node):
        if not node:
            return 0

        left = self.height(node.left)
        if left == -1:
            return -1

        right = self.height(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    def isBalanced(self, root):
        return self.height(root) != -1

   
        
        