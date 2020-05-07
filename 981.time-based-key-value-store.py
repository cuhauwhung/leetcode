#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap(object):

    # key: use bsearch 
    
    def __init__(self):
        self.map = collections.defaultdict(list)
        
    def set(self, key, value, timestamp):
        self.map[key].append((timestamp, value))
        

    def get(self, key, timestamp):
        values = self.map[key]
        if not values: return ''
        left, right = 0, len(values)
        while left < right:
            mid = (left + right) // 2
            pre_time, value = values[mid]

            if pre_time <= timestamp:
                left = mid + 1
                
            elif pre_time > timestamp:
                right = mid

        return "" if right == 0 else values[right - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


  
# @lc code=end

