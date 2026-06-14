import heapq

def solution(n, works):
    # 이미 작업량 합이 n 이하면 모두 0으로 만들 수 있음
    if sum(works) <= n:
        return 0

    # 최대 힙 (음수로 저장)
    heap = [-w for w in works]
    heapq.heapify(heap)

    for _ in range(n):
        largest = -heapq.heappop(heap)
        largest -= 1
        heapq.heappush(heap, -largest)

    return sum(w * w for w in heap)