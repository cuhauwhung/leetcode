#
# @lc app=leetcode id=811 lang=python3
#
# [811] Subdomain Visit Count
#

# @lc code=start
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        from collections import defaultdict
        counter = defaultdict(int)
        
        for cur_domain in cpdomains:
            count, dom = cur_domain.strip().split()
            counter[dom] += int(count)
            
            for i in range(len(dom)):
                if dom[i] == ".":
                    counter[dom[i+1:]] += int(count)

        return ["%d %s" % (counter[k], k) for k in counter]
# @lc code=end

