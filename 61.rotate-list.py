#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return None 

        # have to find length 
        lastElement = head 
        length = 1

        while lastElement.next:
            lastElement = lastElement.next 
            length += 1 

        # take mod, so we don't have to rotate over and over  
        # make the linked list a circle
        k = k % length 
        lastElement.next = head 

        # keep going until the node before at position (length - k), so we can set that element to point to None 
        tempNode = head 
        for _ in range(length - k - 1):
            tempNode = tempNode.next 

        answer = tempNode.next 
        tempNode.next = None 

        return answer 

# @lc code=end

