import sys

def min_ops(s):
    n = len(s)
    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for leng in range(2, n + 1):
        for i in range(n - leng + 1):
            j = i + leng - 1
            delete_left = dp[i + 1][j]
            delete_right = dp[i][j - 1]
            if i + 1 > j - 1:
                replace_or_match = 0
            else:
                replace_or_match = dp[i + 1][j - 1]
            if s[i] == s[j]:
                dp[i][j] = replace_or_match
            else:
                dp[i][j] = 1 + min(delete_left, delete_right, replace_or_match)
    return dp[0][n - 1]

input = sys.stdin.read
data = input().strip()
s = data
n = len(s)
ans = min_ops(s)
for i in range(n):
    for j in range(i + 1, n):
        if s[i] != s[j]:
            ls = list(s)
            ls[i], ls[j] = ls[j], ls[i]
            new_s = ''.join(ls)
            ans = min(ans, min_ops(new_s) + 1)
print(ans)