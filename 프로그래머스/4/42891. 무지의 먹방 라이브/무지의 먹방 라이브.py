import heapq

def solution(food_times, k):
    # 모든 음식을 다 먹는 총 시간보다 k가 크거나 같으면 -1
    if sum(food_times) <= k:
        return -1

    # (남은시간, 음식번호) 형태로 min-heap 구성
    heap = [(t, i + 1) for i, t in enumerate(food_times)]
    heapq.heapify(heap)

    eaten = 0       # 현재까지 소비한 시간
    prev = 0        # 직전에 처리한 음식의 남은 시간
    remaining = len(food_times)  # 아직 남은 음식 수

    while heap:
        time, idx = heap[0]  # 가장 적게 남은 음식

        # 현재 레벨(time - prev)을 remaining개 음식 전부 한 바퀴씩 돌리면 드는 시간
        cycle_cost = (time - prev) * remaining

        if eaten + cycle_cost > k:
            # 이 레벨 안에서 k초가 걸림 → 남은 음식들을 원래 번호 순으로 정렬
            left_time = k - eaten           # 이 레벨에서 남은 시간
            # 아직 heap에 있는 음식들을 번호 순으로 정렬
            candidates = sorted(heapq.nsmallest(remaining, heap), key=lambda x: x[1])
            return candidates[left_time % remaining][1]

        # 이 레벨을 통째로 소비
        eaten += cycle_cost
        prev = time
        remaining -= 1
        heapq.heappop(heap)