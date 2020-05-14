#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
        bulls = 0 
        bucket = [0] * 10 
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1 

            else:
                bucket[int(s)] += 1 
                bucket[int(g)] -= 1 
        
        return '%sA%sB' % (bulls, len(secret) - bulls - sum(cnt for cnt in bucket if cnt>0))

# @lc code=end

