#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_1, set_2 = set(nums1), set(nums2)
        temp = set_1.intersection(set_2)
        return list(temp) 
        
# @lc code=end
