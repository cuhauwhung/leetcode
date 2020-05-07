#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#

# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
         # key: sort people by height and then by k, number of people in front of this person, 
        #      then insert p into a new list based on k
        
        people_sorted = sorted(people, key = lambda x: (-x[0], x[1]))
        res = list()
        for p in people_sorted: 
            res.insert(p[1], p)
        return res 
# @lc code=end

