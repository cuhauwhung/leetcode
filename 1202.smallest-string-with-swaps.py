#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#

# @lc code=start
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        from collections import defaultdict
        def dfs(i):
            visited[i] = True
            component.append(i)
            for j in maps[i]:
                if not visited[j]:
                    dfs(j)
            
        n = len(s)
        maps = defaultdict(list)
        for i, j in pairs:
            maps[i].append(j)
            maps[j].append(i)
            
        visited = [False for _ in range(n)]
        lst = list(s)
        for i in range(n):
            if not visited[i]:
                component = list()
                dfs(i)
                
                component.sort()

                chars = [lst[k] for k in component]
                chars.sort()
                
                for i in range(len(component)):
                    lst[component[i]] = chars[i]
                    
        return ''.join(lst)
        
# @lc code=end
