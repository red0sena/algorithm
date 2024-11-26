import sys


n = int(sys.stdin.readline().rstrip())
ars = []
for _ in range(n):
    num, a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))
    ars.append([a, b, c, num])

ars = sorted(ars, key=lambda x : [x[0] * x[1] * x[2], x[0] + x[1] + x[2], x[3]])


for rank in ars[:3]:
    print(rank[3], end=' ')

