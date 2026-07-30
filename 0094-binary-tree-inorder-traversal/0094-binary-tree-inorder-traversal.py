# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
list = []
class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []
        return (
            self.inorderTraversal(root.left) +
            [root.val] +
            self.inorderTraversal(root.right)
        )
        