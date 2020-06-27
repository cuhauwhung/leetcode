#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        from collections import defaultdict
        res = []
        if not matrix: return res
        lines = defaultdict(list)

        # indexes on a diagonal would have the same i+j
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lines[i+j].append(matrix[i][j])
                
        for k in range(len(matrix) + len(matrix[0]) - 1):
            if k % 2 == 0:
                res += lines[k][::-1]
            else:
                res += lines[k]
        return res

# @lc code=end