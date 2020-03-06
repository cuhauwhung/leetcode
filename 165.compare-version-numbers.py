#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.strip().split(".")
        nums2 = version2.strip().split(".")
        n1, n2 = len(nums1), len(nums2)

        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0 
            i2 = int(nums2[i]) if i < n2 else 0 
            
            if i1 != i2:
                return 1 if i1 > i2 else -1
        
        return 0
# @lc code=end

