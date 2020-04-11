#
# @lc app=leetcode id=1166 lang=python3
#
# [1166] Design File System
#

# @lc code=start

from collections import defaultdict

class TrieNode:
    def __init__(self, val):
        self.children = {} # Note that {key:value}, key is string, value is TrieNode
        self.val = val
        
class FileSystem:
    def __init__(self):
        self.root = TrieNode(0)

    def createPath(self, path: str, value: int) -> bool:

        # Return False: 1. path already exists  2. parent path doesn't exist
        names = path[1:].split('/')
        curr = self.root
        for i, name in enumerate(names):
            
            # last name == need to create 
            if i == len(names)-1: 

                # already exists 
                if name in curr.children:
                    return False
                
                # create new path 
                curr.children[name] = TrieNode(value)
                return True

            # parent path doesn't exist
            if name not in curr.children: 
                return False
                
            curr = curr.children[name]

    def get(self, path: str) -> int:
        curr = self.root
        names = path[1:].split('/')
        for _, name in enumerate(names):
            if name not in curr.children:
                return False
            curr = curr.children[name]
        return curr.val

# @lc code=end