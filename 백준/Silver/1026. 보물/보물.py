import sys

n = int(sys.stdin.readline().rstrip())
a_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
b_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

a_list = sorted(a_list)
b_list = sorted(b_list, reverse=True)
ans = 0
for i in range(0, n):
    ans += a_list[i] * b_list[i]

print(ans)