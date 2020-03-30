#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # key: reverse matrix vertically and then transpose
        # matrix.reverse()
        # print(matrix)
        # for i in range(len(matrix)):
        #     for j in range(i):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        # key: the first loop i is to see how many layers 
        #           the second loop j is to see how many shifts we need 

        n = len(matrix[0])
        for i in range((n+1)//2):
            for j in range(i, n - 1 -i):
                tmp = [0] * 4
                row, col = i, j

                # store 4 elements in tmp
                for k in range(4):
                    tmp[k] = matrix[row][col]
                    row, col = col, n - 1 - row

                # rotate 4 elements   
                for k in range(4):
                    matrix[row][col] = tmp[(k - 1) % 4]
                    row, col = col, n - 1 - row
# @lc code=end

