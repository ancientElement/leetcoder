#
# @lc app=leetcode.cn id=142 lang=python
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        p1,p2 = head,head
        while p1 != p2:
            p1 = p1.next
            if not p1: return None
            if not p2.next: return None
            p2 = p2.next.next
            if not p2: return None
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
        
# @lc code=end
# @km code=start
while(True):
    try:
        arr = [3,2,0,-4]
        tail_to = 1
        tail_to_node = None
        head = None
        cur = head
        for i in range(len(arr)):
            cur = ListNode(arr[i])
            if i == 1: head = cur
            if tail_to == i: tail_to_node = cur
            cur = cur.next
            
        
    except:
# @km code=end
