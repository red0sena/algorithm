import sys


N = int(sys.stdin.readline())
time = []
for i in range(N):
    s, e = map(int, sys.stdin.readline().split())
    time.append([s, e])




time.sort(key = lambda x: (x[1], x[0]))

count = 1 # 이미 맨 처음 회의는 들어가 있다.

meeting_end = time[0][1]

for i in range(1, N):
    if time[i][0] >= meeting_end:
        count += 1
        meeting_end = time[i][1]


print(count)