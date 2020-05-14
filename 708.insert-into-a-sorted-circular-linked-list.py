#
# @lc app=leetcode id=708 lang=python3
#
# [708] Insert into a Sorted Circular Linked List
#

# @lc code=start


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        # key: keep looping until we find suitable place to insertVal
        #      1) inserVal is in between smallest and largest 
        #      2) insertVal is either smallest or largest val 
        #      3) all existing vals are duplicate (made a loop)

        insert_node = Node(insertVal, head)
        
        if not head:
            insert_node.next = insert_node
            return insert_node
        
        cur = head
        
        while 1:
            if cur.val <= insertVal <= cur.next.val:
                break
            elif cur.val>cur.next.val and (insertVal>=cur.val or insertVal<=cur.next.val):
                break
            elif cur.next is head:
                break        
            cur = cur.next
            
        insert_node.next = cur.next
        cur.next = insert_node
        
        return head

# @lc code=end