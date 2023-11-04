import sys 
import heapq


N = int(sys.stdin.readline())
Cards = []
for i in range(N):
    card = int(sys.stdin.readline())
    heapq.heappush(Cards, card)


compare_counts = 0
added_list = []

if N == 1:
    compare_counts = 0
elif N == 2:
    compare_counts = Cards[0] + Cards[1]
else:
    for i in range(0, N-1):
        added = heapq.heappop(Cards) + heapq.heappop(Cards)
        heapq.heappush(Cards, added)
        compare_counts += added
    

print(compare_counts)