#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):

        dummy = p = ListNode(0)
        dummy.next = head 

        # list should contain pointers: (p, h, t) in this order 
        while head and head.next:
            tmp = head.next 
            head.next = tmp.next 
            p.next = tmp
            tmp.next = head 

            # move the head and p pointers to their respective positions 
            head = head.next 
            p = tmp.next 

        return dummy.next 

# @lc code=end