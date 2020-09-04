#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# @lc code=start
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        ans = list()
        left, right = 0, 0
        rightmost = {c:i for i, c in enumerate(S)}

        for i, char in enumerate(S):
            right = max(right, rightmost[char])

            if i == right:
                ans += [right - left + 1]
                left = i + 1 

        return ans 

# @lc code=end