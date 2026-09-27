# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        global ret
        ret = []
        self.helpPathSum(root,0)
        if targetSum in ret:
            return True
        return False

    def helpPathSum(self,u,cur):
        if not u:
            return
        if not u.left and not u.right:
            ret.append(cur + u.val)
        if u.left:
            self.helpPathSum(u.left,cur + u.val)
        if u.right:
            self.helpPathSum(u.right,cur + u.val)
        