#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # key: sort and move left and right to center 
        # if the sum of both values are less than limit, we can group them together, 
        # if not then, we just decrement right, which means right can be be in a group by himself

        people.sort()
        count, n = 0, len(people) 
        left, right = 0, n - 1

        while left <= right: 

            if people[left] + people[right] <= limit: 
                left += 1 
                right -= 1 
            
            else: 
                right -= 1 
            
            count += 1

        return count 
# @lc code=end

