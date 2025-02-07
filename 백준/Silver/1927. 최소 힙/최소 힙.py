import heapq
import sys
n = int(sys.stdin.readline().rstrip())
input_list = []
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(input_list) == 0:
            print(0)
        else:
            a = heapq.heappop(input_list)
            print(a)
    else:
        heapq.heappush(input_list, x)
