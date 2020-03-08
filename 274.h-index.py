#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)

        # papers[i] is the number of papers with i citations.
        papers = [0] * (n + 1) 
        for c in citations:

            # All papers with citations larger than n is count as n.
            papers[min(n, c)] += 1  
 

        print(papers)
        i = n
        s = papers[n]  # sum of papers with citations >= i
        while i > s:
            i -= 1
            s += papers[i]
        return i

        # citations.sort(reverse=True)
        # h_ind = 0
        
        # for ind, cit in enumerate(citations):
        #     if cit > ind:
        #         h_ind += 1
                
        # return h_ind  
# @lc code=end

