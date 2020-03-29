#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        from collections import deque 
        if not root: return None 
        queue = deque()
        queue.append(root)
        queue.append(None)

        while queue:
            
            cur = queue.popleft()

            if cur:
                cur.next = queue[0]
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)

            else:
                if len(queue) > 0:
                    queue.append(None)

        return root



    # @lc code=end

