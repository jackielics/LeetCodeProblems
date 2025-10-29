#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:    
        if not root:
            return 0
        elif not (root.left or root.right):
            return 1
        res = float('inf')
        if root.left:
            res = min(res, 1 + self.minDepth(root.left))
        if root.right:
            res = min(res, 1 + self.minDepth(root.right))
        return res
# @lc code=end

