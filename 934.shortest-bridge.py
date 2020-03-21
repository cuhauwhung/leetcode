#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#

# @lc code=start


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:

        # key: use dfs to find the first island, 
        # then grow one island until it reaches the other using bfs
        
        moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n, steps, bfs = len(A), 0, list()
        
        def dfs(i, j):
            A[i][j] = -1
            bfs.append((i, j))
            for dx, dy in moves:
                new_x, new_y = i + dx, j + dy
                if 0 <= new_x < n and 0 <= new_y < n and A[new_x][new_y] == 1:
                    dfs(new_x, new_y)

        def first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        return i, j

        dfs(*first())
        
        while bfs:
            temp = []
            for i, j in bfs:
                for dx, dy in moves:
                    new_x, new_y = dx + i, dy + j
                    if 0 <= new_x < n and 0 <= new_y < n:
                        if A[new_x][new_y] == 1:
                            return steps

                        elif not A[new_x][new_y]:
                            A[new_x][new_y] = -1
                            temp.append((new_x, new_y))
            steps += 1
            bfs = temp


# @lc code=end
