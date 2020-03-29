#
# @lc app=leetcode id=840 lang=python3
#
# [840] Magic Squares In Grid
#

# @lc code=start
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isSubGridMagic(grid,i,j): 
            nums = set(grid[a][b] for b in range(j,j+3) for a in range(i,i+3) if grid[a][b]>=1 and grid[a][b]<=9)
            a = grid[i][j:j+3]
            b = grid[i+1][j:j+3]
            c = grid[i+2][j:j+3]
            d = [grid[x][j] for x in range(i,i+3)]
            e = [grid[x][j+1] for x in range(i,i+3)]
            f = [grid[x][j+2] for x in range(i,i+3)]
            g = [grid[x+i][y+j] for x in range(3) for y in range(3) if x==y]
            h = [grid[x+i][y+j] for x in range(2,-1,-1) for y in range(3) if x+y==2]
            if sum(a)==sum(b)==sum(c) == sum(d)==sum(e)==sum(f)==sum(g)==sum(h) and len(nums)==9:
                return True
            else:
                return False
        
        
        count=0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if isSubGridMagic(grid,i,j):
                    count+=1
        return count


# @lc code=end

