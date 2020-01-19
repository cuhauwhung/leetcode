#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n, firstRowHasZero = len(matrix), len(matrix[0]), not all(matrix[0])

        # use first row and column as the marker
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0

        # set the corresponding cells with zeros
        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # if first row has zeros, then mark the first row with all zeros
        if firstRowHasZero:
            matrix[0] = [0] * n

# @lc code=end
