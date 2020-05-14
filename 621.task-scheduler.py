#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter 

        # key: schedule the most frequent tasks as frequently as possible. 
        #      Begin with scheduling the most frequent task. 
        #      Then cool-off for n, and in that cool-off period schedule tasks in order of frequency, or if no tasks are available, then be idle.

        curr_time, heap = 0, []
        for v in collections.Counter(tasks).values():
            heapq.heappush(heap, -1*v)
            
        while heap:
            temp = []
            for _ in range(n+1):
                curr_time += 1

                if heap:
                    timing = heapq.heappop(heap)
                    if timing != -1:
                        temp.append(timing+1)
                
                # no values to add, add idle 
                if not temp:
                    break
                    
            for item in temp:
                heapq.heappush(heap, item)
                
        return curr_time



# @lc code=end