#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def comp(left, right):
            if not (left or right):
                return True
            elif (left and right):
                return (left.val == right.val) and comp(left.left, right.right) and comp(left.right, right.left)
            else:
                return False

        return comp(root.left, root.right)
# @lc code=end

