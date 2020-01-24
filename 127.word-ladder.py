#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # key idea: use BFS to check through possible combinations and then if word is not visited and is in the word set then we can just return the height from the queue 

        word_set, visited = set(wordList), set()
        queue = [(beginWord, 1)]

        while queue:

            word, height = queue.pop(0)

            if word == endWord:
                return height
            
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    tmp = word[:i] + j + word[i+1:]
                    if tmp not in visited and tmp in word_set:
                        queue.append((tmp, height + 1))
                        visited.add(tmp)

        return 0 




# @lc code=end