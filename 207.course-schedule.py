#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
            
        # visit each node
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True
        
    def dfs(self, graph, visited, i):
        
        # if ith node is marked as being visited, then a cycle is found
        if visited[i] == -1:
            return False
        
        # if it is done visted, then do not visit again
        if visited[i] == 1:
            return True
        
        # mark as being visited
        visited[i] = -1
        # visit all the neighbours
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False
        # after visit all the neighbors, mark it as done visited
        visited[i] = 1
        return True
        
# @lc code=end

