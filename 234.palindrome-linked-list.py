#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        slow = fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        
        dummy = None 
        while slow:
            nxt = slow.next 
            slow.next = dummy 
            dummy = slow 
            slow = nxt 
            
        while dummy: 
            if dummy.val != head.val:
                return False
            dummy = dummy.next 
            head = head.next 
            
        return True 
# @lc code=end