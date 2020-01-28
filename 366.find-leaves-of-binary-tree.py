#
# @lc app=leetcode id=366 lang=python3
#
# [366] Find Leaves of Binary Tree
#

# @lc code=start
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict

        # key idea: is the lev = max(left, right) + 1 
        #           level here is the distance from the leaves. If the node has no left and no 
        #           right, then its level would be 1. We then utilize the the max of these levels 
        #           for non leaves based on the max(left, right) and then append this info into a
        #           dictionary, which we will return 

        def order(root, this_dict):

            if not root: return 0 
            left = order(root.left, this_dict)
            right = order(root.right, this_dict)
            level = max(left, right) + 1 
            this_dict[level].append(root.val)
            return level 

        this_dict = defaultdict(list)
        order(root, this_dict)
        return [x for x in this_dict.values()]

# @lc code=end