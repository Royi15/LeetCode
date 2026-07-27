# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        result = []
        self.help(root, result)
        return result

    def help(self, node, result):
        if node is None:
            return 
        self.help(node.left, result)
        self.help(node.right, result)
        result.append(node.val)

        