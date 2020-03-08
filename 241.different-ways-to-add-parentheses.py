#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:

        # idea: ways(2*3-4*5) = ways(2) *^* ways(3-4*5) U ways(2*3) *^- ways(4*5) U ways(2*3-4) *^* ways(5)

        if input.isdigit(): return [int(input)]
        ans = list()
        
        for i in range(len(input)):
            if input[i] in "+-*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                
                for j in res1:
                    for k in res2:
                        ans.append(self.helper(j, k, input[i]))
        return ans 
                   
    def helper(self, m, n, op):
        if op == "+": return m + n 
        elif op == "-": return m - n 
        elif op == "*": return m * n 

# @lc code=end

