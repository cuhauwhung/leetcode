#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#

# @lc code=start
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        # key: use max-heap to store "live" building
        #      go from left to right and perform one of 3 operations:
        #      1) remove dead buildings 
        #      2) add new buildings into heap 
        #      3) add result if height is different 

        events = [(L, -H, R) for L, R, H in buildings]
        events += [(R, 0, 0) for L, R, H in buildings]
        events.sort()

        ans = [[0,0]]
        live = [(0, float("inf"))]

        for pos, negH, R in events:

            # remove all "dead" buildings from heap 
            while live[0][1] <= pos: 
                heapq.heappop(live)
            
            # add buildings into the heap 
            if negH:
                heapq.heappush(live, (negH, R))

            # add to result if the previous keypoint height != current keypoint height
            if ans[-1][1] != -live[0][0]:
                ans.append([pos, -live[0][0]])

        return ans[1:]
        
# @lc code=end