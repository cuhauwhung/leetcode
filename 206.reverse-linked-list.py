#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        ## iterative 
        # prev = None 
        # current = head 
        
        # # while list node isn't empty keep moving forward 
        # while current: 
        #     next = current.next
        #     current.next = prev
        #     prev = current
        #     current = next
        # return prev 

        ## recursive 
        return self.helper(None, head)

    def helper(self, prev: ListNode, current: ListNode) -> ListNode:
        if current: 
            next = current.next 
            current.next = prev 
            return self.helper(current, next)

        else:
            return prev 

# @lc code=end

