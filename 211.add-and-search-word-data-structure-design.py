#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#

# @lc code=start

class WordNode:
    def __init__(self):
        self.children = collections.defaultdict(WordNode)
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = WordNode()
        
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root 
        for w in word:
            node = node.children[w] 
        node.isEnd = True         
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        stack = [(self.root,word)]
        while stack:
            node, w = stack.pop()
            if not w:
                if node.isEnd:
                    return True

            elif w[0]=='.':
                for n in node.children.values():
                    stack.append((n,w[1:]))

            else:
                if w[0] in node.children:
                    n = node.children[w[0]]
                    stack.append((n,w[1:]))

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# @lc code=end