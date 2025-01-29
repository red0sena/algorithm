import heapq
import sys
n = int(input())
heap = []
for i in range(n):
    val = int(sys.stdin.readline().rstrip())
    if val != 0:
        heapq.heappush(heap, -val)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))


