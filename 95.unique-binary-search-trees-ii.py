#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        # key: essentially, we go through and test the different roots 
        #       and build a subtree at root.left and root.right with 
        #       values that work! values that work will be placed at left/right positions
        #       no values will be inserted with None

        def dfs(first, last):

            result = list()

            for root in range(first, last+1):
                for l in dfs(first, root - 1) or [None]:
                    for r in dfs(root + 1, last) or [None]:
                        node = TreeNode(root)
                        node.left, node.right = l, r 
                        result.append(node)
            return result 
            
        if not n: return 
        return dfs(1, n)



# @lc code=end

