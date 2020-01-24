#
# @lc app=leetcode id=1181 lang=python3
#
# [1181] Before and After Puzzle
#

# @lc code=start
class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:

        # idea: tokenize all the phrases first and go through them to check  
        res = list()
        s = [st.split(' ') for st in phrases]
        
        for i in range(len(s)):
            for j in range(len(s)):
                if j != i:
                    if s[i][-1] == s[j][0]:
                        res.append(s[i]+s[j][1:])
                        
        out = set([" ".join(w) for w in res])
        
        return sorted(out)


# @lc code=end

