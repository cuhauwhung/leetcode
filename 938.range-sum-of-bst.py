#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        from collections import deque 
        
        ans = 0
        queue = deque()
        queue.append(root)
        
        while queue:
            curr = queue.popleft()
            if L <= curr.val <= R: 
                ans += curr.val
            
            if curr.left:
                queue.append(curr.left)
            if curr.right: 
                queue.append(curr.right)
        
        return ans 
# @lc code=end

