#
# @lc app=leetcode id=636 lang=python3
#
# [636] Exclusive Time of Functions
#

# @lc code=start
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
    
        ans = [0] * n
        stack = []

        for log in logs:
             
            pid, event, time = log.split(':')
            pid, time = int(pid), int(time)

            if event == 'start':
                if len(stack) > 0:
                    ans[stack[-1]] += time - prev_time 
                stack.append(pid)
                prev_time = time

            else:
                ans[stack.pop()] += time - prev_time + 1
                prev_time = time + 1

        return ans

                
# @lc code=end

