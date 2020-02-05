#
# @lc app=leetcode id=611 lang=python3
#
# [611] Valid Triangle Number
#

# @lc code=start
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        n = len(nums)
        ans = 0 
        nums.sort(reverse=True)

        if n < 3: return 0 
        
        for c in range(0, n-2):
            b = c + 1 
            a = n - 1 

            while b < a:
                if nums[a] + nums[b] > nums[c]:
                    ans += a - b 
                    b += 1 
                else:
                    a -= 1 
        return ans 




# @lc code=end
