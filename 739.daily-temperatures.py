#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        ans = [0] * len(T)
        stack = list() 
        for i in range(len(T) - 1, -1, -1):
            
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            
            if len(stack) > 0:
                ans[i] = stack[-1] - i 

            stack.append(i)

        return ans 

# @lc code=end

