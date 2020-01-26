#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
import math 
class Solution:

    def numSquares(self, n: int) -> int:

        if n < 2: return n
        square_nums = [i * i for i in range(1, int(n**0.5)+1)]
    
        level = 0
        queue = {n}

        while queue:
            
            level += 1
            next_queue = set()

            # construct the queue for the next level
            for remainder in queue:
                for square_num in square_nums: 

                    if remainder == square_num:
                        return level  

                    elif remainder < square_num:
                        break

                    else:
                        next_queue.add(remainder - square_num)

            queue = next_queue
        return level


# @lc code=end

