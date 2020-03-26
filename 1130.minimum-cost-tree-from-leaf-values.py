#
# @lc app=leetcode id=1130 lang=python3
#
# [1130] Minimum Cost Tree From Leaf Values
#

# @lc code=start
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        # key: 1) Pick up the leaf node with minimum value
        #      2) Combine it with its inorder neighbor which has smaller value between neighbors
        #      3) Once we get the new generated non-leaf node, the node with minimum value is useless 
        #      4) Repeat it until there is only one node.

        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i - 1:i] + arr[i+1:i+2]) * arr.pop(i)
        return res

# @lc code=end

