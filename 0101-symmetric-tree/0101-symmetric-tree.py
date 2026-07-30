# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.help(root.left,root.right)

    def help(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and (self.help(left.right,right.left)) and (self.help(left.left,right.right))
        
        