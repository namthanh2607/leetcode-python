# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        global ret
        ret = []
        if not root:
            return []
        self.helpPathSum(root,[root.val],targetSum)
        return ret

    def helpPathSum(self,u,lst,targetSum):
        if not u:
            return
        if not u.left and not u.right and sum(lst) == targetSum:
            ret.append(lst)
        if u.left:
            self.helpPathSum(u.left,lst + [u.left.val],targetSum)
        if u.right:
            self.helpPathSum(u.right,lst + [u.right.val],targetSum)
        