import heapq
n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))

while heap:
    print(heapq.heappop(heap))
