#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import defaultdict

        sequences = defaultdict(int) 
        for i in range(len(s)):
            sequences[s[i:i+10]] += 1
        return [key for key, value in sequences.items() if value > 1] 

# @lc code=end

