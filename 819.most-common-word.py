#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#

# @lc code=start
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import Counter 
        wordCount = Counter()
        removePunctuationTable = str.maketrans("!?',;.", "      ")
        paragraph = paragraph.translate(removePunctuationTable)
        
        banned = set(banned)
        for word in paragraph.split():
            word = word.lower()
            if word not in banned:
                wordCount[word] += 1
        return wordCount.most_common(1)[0][0]



# @lc code=end

