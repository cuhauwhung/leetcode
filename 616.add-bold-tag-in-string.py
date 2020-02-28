#
# @lc app=leetcode id=616 lang=python3
#
# [616] Add Bold Tag in String
#

class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        
        # find the locations of dict_words in s 
        # and get the intervals 
        location = list()
        for word in dict:
            start = s.find(word)
            while start != -1:
                location.append([start, start + len(word)])
                start = s.find(word, start + 1)
        if not location: return s 
        location.sort(key=lambda x: x[0])
        
        # merge intervals and add the tags
        st, e = location[0][0], location[0][1]
        res = s[0:st]
        
        for x in range(1, len(location)):
            if location[x][0] <= e:
                e = max(e, location[x][1])
            else:
                res += "<b>" + s[st:e] + "</b>"
                res += s[e:location[x][0]]
                st, e  = location[x][0], location[x][1]
        res += "<b>" + s[st:e] + "</b>" + s[e:]
        return res

# @lc code=end