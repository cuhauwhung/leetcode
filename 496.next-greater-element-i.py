#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        d = dict()
        for i in nums2:
            while stack and stack[-1] < i:
                j = stack.pop()
                d[j] = i
            stack.append(i)
        return [d.get(i, -1) for i in nums1]
        
# @lc code=end

