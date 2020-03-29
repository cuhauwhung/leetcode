#
# @lc app=leetcode id=855 lang=python3
#
# [855] Exam Room
#

# @lc code=start

class ExamRoom:
    # key: have to maximize distance between every pair of students in exam room 
    
    def __init__(self, N: int):
        self.num = N 
        self.seats = list()

    def seat(self) -> int:
        n, seats = self.num, self.seats 
        if not seats:
            pos = 0 

        else:
            opt_dist, pos = seats[0], 0 
            for a, b in zip(seats, seats[1:]):
                new_dist = (b - a) // 2

                if new_dist > opt_dist: 
                    opt_dist, pos = new_dist, a + new_dist 
        
            if n - 1 - seats[-1] > opt_dist:
                pos = n - 1 

        bisect.insort(self.seats, pos)
        return pos 

    def leave(self, p: int) -> None:
        self.seats.remove(p)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)

# @lc code=end