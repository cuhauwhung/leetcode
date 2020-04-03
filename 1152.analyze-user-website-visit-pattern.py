#
# @lc app=leetcode id=1152 lang=python3
#
# [1152] Analyze User Website Visit Pattern
#

# @lc code=start

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        from collections import defaultdict, Counter

        # key: use the combinations function to obtain 
        #      combinations of list and then just add to the counter
        #      sort final counter by counts and then lexically
        
        by_user = defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            by_user[u].append(w)
            
        count = Counter()
        for cur_vals in by_user.values():
            count += Counter(set(combinations(cur_vals, 3)))

        return min(count, key=lambda k: (-count[k], k))

# @lc code=end
