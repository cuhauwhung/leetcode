#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # key idea: purpose of the stack is to find possible s2 values and then 
        #           get rid of values that can act as s3, since we are popping values that 
        #           are smaller than n 

        stack = []
        s3 = float('-Inf')
        for n in nums[::-1]:

            if n < s3:
                return True

            while stack and stack[-1] < n:
                s3 = stack.pop()

            stack.append(n)

        return False



# @lc code=end

