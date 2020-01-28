#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if not head: return 

        odd = head 
        even, second_node = head.next, head.next 

        while odd.next and even.next:
            odd.next = odd.next.next 
            if odd.next: odd = odd.next 
            even.next = even.next.next 
            if even.next: even = even.next

        odd.next = second_node 

        return head 
        
# @lc code=end