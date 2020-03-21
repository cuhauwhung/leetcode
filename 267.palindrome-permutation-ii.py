#
# @lc app=leetcode id=267 lang=python3
#
# [267] Palindrome Permutation II
#

# @lc code=start

class Solution:
    def generatePalindromes(self, s: str) -> List[str]:

        # key: use dfs backtracking to get the permutations 
        # number of odds should be 1, if not 1, then something wrong.
        # if it is 1, then start with that value to perform backtracking
        
        from collections import Counter
        ans = []
        n = len(s)
        counter = Counter(s)
        
        def helper(tmp):
            if len(tmp) == n:
                ans.append(tmp)
                return 

            for k, v in counter.items():
                if v > 0:
                    counter[k] -= 2
                    helper(k + tmp + k)
                    counter[k] += 2
        
        odd = [key for key, value in counter.items() if value & 1]
        if len(odd) > 1:
            return []
        
        if len(odd) == 1:
            counter[odd[0]] -= 1
            helper(odd[0])
            
        else:
            helper('')
            
        return ans


# @lc code=end

