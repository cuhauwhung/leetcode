#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        from collections import deque
        if not rooms: return 
        r, c= len(rooms), len(rooms[0])
        
        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    queue = deque([(i+1, j, 1), (i-1, j, 1), (i, j+1, 1), (i, j-1, 1)])
                    while queue:
                        x, y, val = queue.popleft()
                        if x < 0 or x >= r or y < 0 or y >= c or rooms[x][y] <= val:
                            continue
                        rooms[x][y] = val
                        queue.extend([(x+1, y, val+1), (x-1, y, val+1), (x, y+1, val+1), (x, y-1, val+1)])

# @lc code=end