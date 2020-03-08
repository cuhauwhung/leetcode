#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = count =  i = 0 

        for j in range(len(nums)):

            # if cur_char is odd
            if nums[j] & 1:
                k -= 1 
                count = 0 
            
            while k == 0:
                k += nums[i] & 1 
                i += 1 
                count += 1 
            res += count 

        return res 
# @lc code=end

