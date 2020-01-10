#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None or l2 is None:
            return False

        dummy = current = ListNode(0)
        carry = 0 

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next 

            if l2: 
                carry += l2.val
                l2 = l2.next 

            current.next = ListNode(carry % 10)
            current = current.next 
            carry = carry // 10

        return dummy.next 
        


# @lc code=end