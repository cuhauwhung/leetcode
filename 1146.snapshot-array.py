#
# @lc app=leetcode id=1146 lang=python3
#
# [1146] Snapshot Array
#

# @lc code=start
class SnapshotArray:

    # key: record the history of each cell. 
    # For each A[i], we will record its history
    # With a snap_id and a its value. 
    # bsearch the time point 
    
    def __init__(self, length: int):
        self.A = [[[-1, 0]] for _ in range(length)]
        self.snap_id = 0
         
    def set(self, index: int, val: int) -> None:
        self.A[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        i = bisect.bisect(self.A[index], [snap_id+1]) - 1 
        return self.A[index][i][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
# @lc code=end

