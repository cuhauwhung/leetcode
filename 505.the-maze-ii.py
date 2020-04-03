#
# @lc app=leetcode id=505 lang=python3
#
# [505] The Maze II
#

# @lc code=start

class Solution:
    def shortestDistance(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        queue, stopped = [(0, start[0], start[1])], {(start[0], start[1]):0}
        moves = [(0,1), (1,0), (-1,0), (0,-1)]

        while queue:
            
            dist, x, y = heapq.heappop(queue)
            if [x, y] == destination: return dist

            for dx, dy in moves:
                d = 0 
                newx, newy = x, y
                while 0 <= newx + dx < m and 0 <= newy + dy < n and maze[newx + dx][newy + dy] != 1:
                    newx += dx
                    newy += dy
                    d += 1

                if (newx, newy) not in stopped or dist + d < stopped[(newx, newy)]:
                    stopped[(newx, newy)] = dist + d
                    heapq.heappush(queue, (dist + d, newx, newy))
        return -1
