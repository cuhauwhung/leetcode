#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter 
        from heapq import heappush, heappop

        # Task map to store if we've seen the item before
        task_count = Counter(tasks)
        current_time = 0
        current_heap = []
        
        # Sorting from least to greatest inside of the heap current_heap
        for k, v in task_count.items():

            # Pushes item from least to greatest (hence the negative values)
            heappush(current_heap, (-v, k)) 
        
        # Here we're running through the entire heap and processing the sorted tasks. Run until the list runs out
        while current_heap: 

            index, temp = 0, []

            while index <= n:

                # count interval time
                current_time += 1 

                if current_heap:
                    timing, taskid = heappop(current_heap)

                    # We're checking to see if it's at the end of the overall count. 
                    if timing != -1:
                        temp.append((timing + 1, taskid))

                # Checking to see if we're out of tasks. Exit the inner loop if both are true.
                if not current_heap and not temp:  
                    break
                else:
                    index += 1

            # Because we transfered all of the items from the heap to temp, we're transferring the updated one back to the heap to know if we should continue
            for item in temp:
                heappush(current_heap, item)

        return current_time  
# @lc code=end

