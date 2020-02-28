#
# @lc app=leetcode id=593 lang=python3
#
# [593] Valid Square
#

# @lc code=start
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        counter = set()
        
        for i in range(3):
            for j in range(i + 1, 4):
                len_sq = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                if len_sq == 0:
                    return False
                else:
                    counter.add(len_sq)
        print(counter)
        return len(counter) == 2 
# @lc code=end

