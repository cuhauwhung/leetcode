#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        x = 0 
        for i in counter:
            nums[x] = i 
            x += 1 

        return len(counter)
        
# @lc code=end