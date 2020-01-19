#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head 
        curr = head 
        total_len = 0
    
        # get length of list
        while curr:
            curr = curr.next 
            total_len += 1 
        
        # get difference 
        x = total_len - n 
        prev, curr = dummy, dummy.next 

        # keep moving until the correct position
        for _ in range(0, x):
            curr = curr.next 
            prev = prev.next 

        prev.next = curr.next
        return dummy.next  
# @lc code=end

