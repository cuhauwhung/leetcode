#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter        
        ans, set_1 = list(), Counter(nums1)

        for i in nums2: 
            if set_1[i] != 0:
                set_1[i] -= 1
                ans.append(i)
                
        return ans
# @lc code=end

