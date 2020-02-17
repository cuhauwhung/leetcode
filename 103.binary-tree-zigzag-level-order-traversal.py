#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
                
        if not root: return 
        queue = [root]
        ans = list()
        level = 0 
        
        while queue:

            temp = list()
            for _ in range(len(queue)):
                
                cur_node = queue.pop(0)
                temp.append(cur_node.val)
                
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            
            temp = temp[::-1] if level % 2 else temp
            ans.append(temp)
            level += 1 
            
        return ans  
# @lc code=end

