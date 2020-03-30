#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        # key:
        #         a1 - a2 - \
        #                     c1 -c2
        #      b1 - b2 - b3 /
        #  
        # a1 - a2 - c1 - c2 - b1 - b2 - b3 - c1
        # b1 - b2 - b3 - c1 - c2 - a1 - a2 - c1 

        if headA is None or headB is None:
            return None

        pa = headA 
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None

# @lc code=end

