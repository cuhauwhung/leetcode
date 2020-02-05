#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        heap = []  # stores the end time of intervals
        
        for i in sorted_intervals:
            if heap and i[0] >= heap[0]: 
                # means two intervals can use the same room
                heapq.heapreplace(heap, i[1])
                
            else:
                # a new room is allocated
                heapq.heappush(heap, i[1])
                
        return len(heap)


# @lc code=end

