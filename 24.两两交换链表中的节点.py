# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode()
        dummy.next = head
        p1 = dummy
        p2 = head
        while p2:
            p3 = p2.next
            if not p3: break 
            p4 = p3.next
            p1.next = p3
            p3.next = p2
            p2.next = p4  
            p1 = p2
            p2 = p4         
        return dummy.next
# @lc code=end

