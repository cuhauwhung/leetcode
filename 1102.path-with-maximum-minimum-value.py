#
# @lc app=leetcode id=1102 lang=python3
#
# [1102] Number of Dice Rolls With Target Sum
#

# @lc code=start

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        R, C = len(A), len(A[0])
        
        maxHeap = [(-A[0][0], 0, 0)]
        seen = [[0 for _ in range(C)] for _ in range(R)]
        while maxHeap:
            val, x, y = heapq.heappop(maxHeap)
            if x == R - 1 and y == C - 1: return -val
            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C and not seen[nx][ny]:
                    seen[nx][ny] = 1 
                    heapq.heappush(maxHeap, (max(val, -A[nx][ny]), nx, ny))
        return -1


        
        
        
        
        
        
        
# @lc code=end
        