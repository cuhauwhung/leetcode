#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # find the midpoint
        if not head: return 
        slow = fast = head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        # reverse the second half 
        pre, node = None, slow
        while node:
            pre, node.next, node = node, pre, node.next  
        
        # merge both in place 
        first, second = head, pre
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next 

        return head 

# @lc code=end