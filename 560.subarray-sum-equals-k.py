#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # key: use prefix sum 
        #      whenever the sums has increased by a value of k, we've found a subarray of sums=k.
        #      keep track of the total sum and use the value (total_sum + nums[i] - total_sum) and store
        #      that difference into a dictionary. At the end, obtain how many times this difference (count) has appeared 
        
        sums, count = 0, 0 
        d = {0: 1}

        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums - k, 0)
            d[sums] = d.get(sums, 0) + 1
        return count

# @lc code=end