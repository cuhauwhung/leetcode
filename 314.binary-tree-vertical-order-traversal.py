#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        from collections import deque

        # use bfs 
        if not root: return []
        res = defaultdict(list)
        queue = list()
        queue.append((root,0))
        while queue:
            node, id = queue.pop(0)
            res[id].append(node.val)
            if node.left:
                queue.append((node.left,id-1))
            if node.right:
                queue.append((node.right,id+1))
        return [res[k] for k in sorted(res.keys())]

        # # slow solution
        # from collections import defaultdict
        # def dfs(root, x_pos, y_pos, ans):
            
        #     if not root:
        #         return None 
            
        #     ans[x_pos].append((root.val, y_pos))
        #     if root.left:
        #         dfs(root.left, x_pos -1, y_pos + 1, ans)
        #     if root.right:
        #         dfs(root.right, x_pos + 1, y_pos + 1, ans)

        # ans = defaultdict(list)
        # dfs(root, 0, 0, ans)
        # final = [[x[0] for x in sorted(k, key = lambda x: x[1])] for k in [ans[k] for k in sorted(ans.keys())]]
        # return final
         
# @lc code=end

