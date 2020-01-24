#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
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

    #     ans = False
    #     for row in matrix:
    #         print(row)
    #         if not row or row[0] > target or ans == True:
    #             return ans
    #         ans = self.targetInRow(row, target)
    #     return ans
    
    # def targetInRow(self, row, target):
    #     left, right = 0, len(row)-1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         cur = row[mid]
    #         print(cur, end = ' ')
    #         if cur == target:
    #             return True
    #         elif cur < target:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #     return False


# @lc code=end
