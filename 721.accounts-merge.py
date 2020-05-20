#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # key: use DFS
        #      make graph and do DFS on each account

        from collections import defaultdict
        visited_accounts = [False] * len(accounts)
        emails_accounts_map = defaultdict(list)
        res = []

        # Build up the graph.
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                emails_accounts_map[email].append(i)

        def dfs(i, emails):
            if visited_accounts[i]: return 
            visited_accounts[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)

                for nei in emails_accounts_map[email]:
                    dfs(nei, emails)
                
        # perform dfs on each account and add to results 
        for i, account in enumerate(accounts):
            if visited_accounts[i]: continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res

# @lc code=end