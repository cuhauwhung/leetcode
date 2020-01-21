#
# @lc app=leetcode id=539 lang=python3
#
# [539] Minimum Time Difference
#

# @lc code=start
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        for i, timePoint in enumerate(timePoints):
            hours, mins = timePoint.split(':')
            timeInMins = int(hours) * 60 + int(mins)
            timePoints[i] = timeInMins
            
        timePoints.sort()
        smallestDiff = float('Inf')
        
        #Compare contiguous pairs and update smallest time difference if necessary.
        for i in range(1, len(timePoints)):
            smallestDiff = min(smallestDiff, timePoints[i] - timePoints[i - 1])
            
        #Special case: smallest difference may occur between largest time and smallest time by wrapping around past midnight.
        print(timePoints[-1], timePoints[0])
        smallestDiff = min(smallestDiff, 60 * 24 - timePoints[-1] + timePoints[0])
        
        return smallestDiff

# @lc code=end

