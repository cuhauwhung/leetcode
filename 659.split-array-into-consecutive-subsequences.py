#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#

# @lc code=start
class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        # key: use greedy. Try to append num into existing open subsequence
        #      if can't make a new subsequence. If can't return False 

        from collections import Counter 
        left = Counter(nums)
        end = Counter()

        for i in nums:

            if left[i] == 0:
                continue
            
            left[i] -= 1 

            if end[i-1] > 0:
                end[i-1] -= 1 
                end[i] += 1 
            
            elif left[i+1] and left[i+2]:
                left[i+1] -= 1
                left[i+2] -= 1
                end[i + 2] += 1 

            else:
                return False

        return True 

        
# @lc code=end

