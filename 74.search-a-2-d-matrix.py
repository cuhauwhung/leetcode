#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0: return False 
        
        h = len(matrix)
        w = len(matrix[0])
        
        row = h - 1 
        col = 0 
        
        while col < w and row >= 0:
            if matrix[row][col] > target: 
                row -= 1 
            elif matrix[row][col] < target: 
                col += 1
            else:
                return True
        return False   
# @lc code=end

