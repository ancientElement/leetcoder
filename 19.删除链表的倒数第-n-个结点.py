# @lc app=leetcode.cn id=19 lang=python
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0,head)
        p1,p2 = dummy,dummy
        for i in range(n):
            p2 = p2.next
        while p2.next:
            p1,p2 = p1.next,p2.next
        p1.next = p1.next.next
        return dummy.next
# @lc code=end

