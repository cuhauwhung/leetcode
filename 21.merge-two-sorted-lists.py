#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # recursive
        # if l1 and l2:
        #     if l1.val < l2.val:
        #         l1, l2 = l2, l1
        #     l1.next = self.mergeTwoLists(l1.next, l2)
        # return l1 or l2
        
        # iterative 
        dummy_head = ListNode(0)
        current = dummy_head  
        
        while l1 and l2:
            if l1.val < l2.val: 
                current.next = l1 
                l1 = l1.next 
                current = current.next

            else:
                current.next = l2 
                l2 = l2.next
                current = current.next

        current.next = l1 if l1 else l2 if l2 else None
        return dummy_head.next 
        
# @lc code=end

