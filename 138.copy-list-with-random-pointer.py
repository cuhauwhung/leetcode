#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        # key: we have to go through all the nodes once to store the listnodes into the hashmap. 
        # Then we have to go through them a second time to actual map the positions of the nodes into the nodes in the hashmap!

        if head is None: return None
        mapping = dict()

        curr = head 
        while curr:
            mapping[curr] = Node(curr.val, None, None)
            curr = curr.next 

        curr = head 
        while curr:
            if curr.next:
                mapping[curr].next = mapping[curr.next]

            if curr.random:
                mapping[curr].random = mapping[curr.random]

            curr = curr.next 

        return mapping[head]
# @lc code=end