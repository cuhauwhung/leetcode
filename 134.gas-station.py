#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # key idea: if the sum(gas) >= sum(cost), there must exist a starting position that allows us to start our travels. If the gas we add + our tank is less than the cost, then this shouldn't be the starting position, thus we should move start one to the right and start the tank from 0. Else, just keep adding into the tank and removing the cost  
        if sum(gas) < sum(cost): return -1

        start, tank = 0, 0
        for i in range(len(gas)):
            if gas[i] + tank < cost[i]:
                start, tank = i + 1, 0
            else:
                tank += gas[i]-cost[i]

        return start

# @lc code=end

