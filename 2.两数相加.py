#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 暴力法
        # carry = 0
        # dummy = ListNode(0)
        # cur = dummy
        # while l1 or l2 or carry:
        #     if l1:
        #         carry += l1.val
        #         l1 = l1.next
        #     if l2:
        #         carry += l2.val
        #         l2 = l2.next
        #     cur.next = ListNode(carry % 10)
        #     cur = cur.next
        #     carry //= 10
        # return dummy.next
        # 2. 递归
        def add(l1, l2, carry):
            if not l1 and not l2 and not carry:
                return None
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            cur = ListNode(val % 10)
            cur.next = add(l1, l2, val // 10)
            return cur
        return add(l1, l2, 0)

# @lc code=end

