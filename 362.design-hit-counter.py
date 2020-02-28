#
# @lc app=leetcode id=362 lang=python3
#
# [362] Design Hit Counter
#

# @lc code=start

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self.counter = deque()

        
    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.counter.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.counter and timestamp - self.counter[0] >= 300:
            self.counter.popleft()
        return len(self.counter)

