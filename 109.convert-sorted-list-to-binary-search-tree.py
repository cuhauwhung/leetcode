#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def findMiddle(self, head):

        # The pointer used to disconnect the left half from the mid node.
        prevPtr = None
        slowPtr = head
        fastPtr = head

        # Iterate until fastPr doesn't reach the end of the linked list.
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        # This is to "break" the lists into two parts. Handles case where slowPtr == head 
        if prevPtr: 
            print(prevPtr.val)
            prevPtr.next = None

        return slowPtr
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        if not head: return None 
        mid = self.findMiddle(head)
        node = TreeNode(mid.val)

        # base case when there's only one element in linked list 
        if head == mid: return node 

        # recursively build the left and right subtrees
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node 

# @lc code=end

