#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#

# @lc code=start
class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        from collections import defaultdict

        # key:  make a dict of all the idxs of each char in S,
        # then we go through each word and find if we can find a suitable idx 
        # for the current c and keep going until the end of the word 
        # break if we no idxs for current c exists or if we can't find a search_idx for the 
        # suffix of the word (search_idx > the last_idx of a c) 

        def isMatch(word, cur_word_idx, search_idx):
            if len(word) == cur_word_idx: return True 
            char_idxs = mapping[word[cur_word_idx]]
            if len(char_idxs) == 0 or search_idx > char_idxs[-1]: return False
            new_pos = char_idxs[bisect_left(char_idxs, search_idx)]
            return isMatch(word, cur_word_idx + 1, new_pos + 1)

        mapping = defaultdict(list)
        for i, c in enumerate(S):
            mapping[c].append(i)

        return sum(isMatch(word, 0, 0) for word in words)
            


# @lc code=end

