#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pa, pb = headA, headB
        res = None
        # 先遍历A
        while pa:
            pa.vst = True
            pa = pa.next
        while pb:
            if hasattr(pb, "vst"):
                res = pb
                break
            pb = pb.next
        # 取消标注
        while pa:
            del pa.vst
            pa = pa.next
        return res

# @lc code=end

