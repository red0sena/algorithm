import heapq

n, m = map(int, input().split())


input_list = list(map(int, input().split()))


heapq.heapify(input_list)

for i in range(m):
    result1 = heapq.heappop(input_list)
    result2 = heapq.heappop(input_list)
    a = result1 + result2
    heapq.heappush(input_list, a)
    heapq.heappush(input_list, a)

print(sum(input_list))
