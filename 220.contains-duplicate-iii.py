#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        if t < 0: return False

        cached = dict()
        for i in range(len(nums)):
            
            if i - k > 0: 
                cached_index = nums[i-k-1] // (t+1)
                del cached[cached_index]

            bucket_index = nums[i] // (t+1)
            cond_1 = (bucket_index in cached)
            cond_2 = ((bucket_index - 1 in cached and abs(nums[i] - cached[bucket_index - 1]) <= t ))
            cond_3 = ((bucket_index + 1 in cached and abs(nums[i] - cached[bucket_index + 1]) <= t ))
            if cond_1 or cond_2 or cond_3: return True
            cached[bucket_index] = nums[i]
            
        return False

# @lc code=end

