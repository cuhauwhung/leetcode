#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#

# @lc code=start
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        # key: use DP to keep track of words that have appeared  
        #      in the dictionary
        
        longest = 1
        d = dict()
        for word in words:
            d[word] = 1

        for word in sorted(words, key=len):
            for i in range(len(word)):
                temp = word[:i] + word[i+1:]
                if temp in d:
                    d[word] = max(d[word], d[temp] + 1)
            longest = max(longest, d[word])
        return longest 

# @lc code=end

