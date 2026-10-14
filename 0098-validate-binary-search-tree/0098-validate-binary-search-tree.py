# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if not root.left and not root.right:
            return True

        return self.help_valid(root, -2**31 - 1, 2**31)
    
    def help_valid(self, node, cur_min, cur_max):
        if not node:
            return True

        if not (cur_min < node.val < cur_max):
            return False

        left_valid = self.help_valid(node.left, cur_min, node.val)
        right_valid = self.help_valid(node.right, node.val, cur_max)

        return left_valid and right_valid

