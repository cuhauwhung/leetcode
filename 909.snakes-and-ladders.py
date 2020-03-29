#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# @lc code=start
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        from collections import deque 

        # key: we have to convert label -> coordinates 
        #      use BFS to find shortest path 

        n = len(board)
        def label_to_position(label):
            r, c = divmod(label-1, n)
            if r % 2 == 0:
                return n-1-r, c
            else:
                return n-1-r, n-1-c
            
        seen = set()
        queue = deque()
        queue.append((1, 0))
        
        while queue:
            
            label, step = queue.popleft()
            x, y = label_to_position(label)
            
            if board[x][y] != -1:
                label = board[x][y]
                
            if label == n*n:
                return step
            
            for dx in range(1, 7):
                new_label = label + dx
                if new_label <= n*n and new_label not in seen:
                    seen.add(new_label)
                    queue.append((new_label, step+1))
        return -1

# @lc code=end

