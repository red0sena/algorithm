import sys
n, k = map(int, sys.stdin.readline().rstrip().split())

input_list = list(map(int, sys.stdin.readline().rstrip().split()))
prefix = [0]
for i in range(n):
    prefix.append(prefix[i] + input_list[i])

res = -int(10e10)
for i in range(k, n+1):
    a = prefix[i] - prefix[i-k]
    res = max(res, a)

print(res)

