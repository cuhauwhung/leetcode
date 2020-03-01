#
# @lc app=leetcode id=729 lang=python3
#
# [729] My Calendar I
#

# @lc code=start
class MyCalendar:

    def __init__(self):
        self.bookings = [[-1, -1], [float('Inf'), float('Inf')]] 

    def book(self, start: int, end: int) -> bool:

        curr = [start, end]
        idx = bisect.bisect(self.bookings, curr)
        if self.bookings[idx-1][1] <= curr[0] and curr[1] <= self.bookings[idx][0]:
            self.bookings.insert(idx, curr)
            return True
        else:
            return False
        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# @lc code=end

