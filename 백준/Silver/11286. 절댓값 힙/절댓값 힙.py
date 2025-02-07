import heapq
import sys
n = int(sys.stdin.readline().rstrip())
minus_heap = []
plus_heap = []
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(plus_heap) == 0 and len(minus_heap) == 0:
            print(0)
        elif len(plus_heap) == 0:
            minus = heapq.heappop(minus_heap)
            print(-minus)
        elif len(minus_heap) == 0:
            plus = heapq.heappop(plus_heap)
            print(plus)
        else:
            minus = heapq.heappop(minus_heap)
            plus = heapq.heappop(plus_heap)
            if minus == plus:
                print(-minus)
                heapq.heappush(plus_heap, plus)
            elif minus > plus:
                print(plus)
                heapq.heappush(minus_heap, minus)
            else:
                print(-minus)
                heapq.heappush(plus_heap, plus)
    else:
        if x > 0:
            heapq.heappush(plus_heap, x)
        else:
            heapq.heappush(minus_heap, -x)
