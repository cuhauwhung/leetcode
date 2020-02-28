#
# @lc app=leetcode id=1197 lang=python3
#
# [1197] Minimum Knight Moves
#

# @lc code=start
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        if x == y == 0: return 0
        moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

        queue = [(0, 0)]
        step = 0
        visited = set()
        x, y = abs(x), abs(y)

        while queue: 

            step += 1 
            for _ in range(len(queue)):
                curX, curY = queue.pop(0)

                for dx, dy in moves:
                    newX, newY = curX + dx, curY + dy

                    if (newX, newY) == (x ,y): 
                        return step 
                    
                    if newX < -2 or newY < -2 or (newX, newY) in visited:
                        continue 

                    visited.add((newX, newY))
                    queue.append((newX, newY))
            
        return step

# @lc code=end