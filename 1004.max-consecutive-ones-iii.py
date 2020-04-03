#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        
        # key: For each A[right], try to find the longest subarray.
        #      If A[left] ~ A[right] has zeros <= K, we continue to increment right.
        #      If A[left] ~ A[right] has zeros > K, we increment left.

        left = 0
        for right in range(len(A)):

            # If we included a zero in the window we reduce the value of K.
            # Since K is the maximum zeros allowed in a window.
            K -= 1 - A[right]

            # A negative K denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if K < 0:
                # If the left element to be thrown out is zero we increase K.
                K += 1 - A[left]
                left += 1
        return right - left + 1
# @lc code=end