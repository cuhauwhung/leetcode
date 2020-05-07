#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # key: use bsearch, but modify with k 

        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2

            # mid + k is closer to x, assign left = mid + 1
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1 
            else:
                right = mid 

        return arr[left: left+k]
            

# @lc code=end

