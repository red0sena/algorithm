import sys


n = int(sys.stdin.readline().rstrip())
sys.setrecursionlimit(10 ** 6)
input_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

dp = [-1] * n


def recursive(index, previous, depth):
    if index >= n:
        return 0

    if dp[index] != -1:
        return dp[index]

    if index != 0 and input_list[index] <= previous:
        return 0

    if index == len(input_list):
        return 1

    max_value = 0
    value_list = []

    for i in range(index+1, n):
        next_value = recursive(i, input_list[index], depth+1)
        value_list.append(next_value)

    value_list.append(max_value)
    max_value = max(value_list)
    dp[index] = 1 + max_value

    return dp[index]

for i in range(n):
    recursive(i, 0, 0)
    
print(max(dp))