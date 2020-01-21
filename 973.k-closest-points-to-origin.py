#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def find_distance(point):
            x, y = point[0], point[1]
            distance = math.sqrt(x * x + y * y) 
            return distance 
            
        info = list()
        for this_point in points:
            distance = find_distance(this_point)
            info.append((this_point, distance))
            
        sorted_info = sorted(info, key = lambda x: x[1])        
        return [sorted_info[x][0] for x in range(0, K)] 
# @lc code=end

