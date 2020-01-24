#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
import random 
class RandomizedSet:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashTable = dict()
        self.arr = list()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        if val not in self.hashTable:
            self.hashTable[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False


    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.hashTable:

            # this is just to reorganize positions between hashmap and array
            idx, last = self.hashTable[val], self.arr[-1]
            self.arr[idx], self.hashTable[last] = last, idx

            self.arr.pop()
            self.hashTable.pop(val, 0)
            return True

        return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.arr[random.randint(0, len(self.arr) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

