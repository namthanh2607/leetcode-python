# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ret = []
        self.helper(root, root.val, 1,ret)
        ans = 0
        for [i,j,k] in ret:
            if i == j//k:
                ans += 1
        return ans
    
    def helper(self, u, total, counts,ret):
        if not u.left and not u.right:
            ret.append([u.val,u.val,1])
            return [u.val,u.val,1]
        
        elif u.right and u.left:
            sum1 = self.helper(u.left, total, count,ret)
            sum2 = self.helper(u.right, total, count,ret)
            print(sum1,sum2)
            ret.append([u.val, sum1[1] + sum2[1] + u.val, sum1[2] + sum2[2] + 1] )
            return [u.val, sum1[1] + sum2[1] + u.val, sum1[2] + sum2[2] + 1] 
        
        elif u.right:
            sum2 = self.helper(u.right, total, count,ret)
            print(sum2)
            ret.append([u.val, sum2[1] + u.val, sum2[2] + 1] )
            return [u.val,  sum2[1] + u.val,  sum2[2] + 1]

        elif u.left:
            sum1 = self.helper(u.left, total, count,ret)
            print(sum1)
            ret.append([u.val, sum1[1] + u.val, sum1[2] + 1] )
            return [u.val,  sum1[1] + u.val,  sum1[2] + 1]

        