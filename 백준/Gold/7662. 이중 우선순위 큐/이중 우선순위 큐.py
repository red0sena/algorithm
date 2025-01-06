import sys
import heapq

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    k = int(input().rstrip())
    min_heap = []
    max_heap = []
    is_valid = dict()  # 값별로 '살아있는' 개수를 관리

    for _ in range(k):
        op, num = input().split()
        num = int(num)

        if op == 'I':
            # 두 힙에 모두 삽입
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            # is_valid에 개수 추가
            is_valid[num] = is_valid.get(num, 0) + 1

        else:  # 삭제 연산
            if not is_valid:
                # 비어있으면 무시
                continue

            if num == 1:
                # 최댓값 삭제 -> max_heap에서 pop
                while max_heap:
                    val = -heapq.heappop(max_heap)
                    if is_valid.get(val, 0) > 0:
                        # 유효한 값이면 1개 줄이고 break
                        is_valid[val] -= 1
                        if is_valid[val] == 0:
                            del is_valid[val]
                        break
            else:
                # 최솟값 삭제 -> min_heap에서 pop
                while min_heap:
                    val = heapq.heappop(min_heap)
                    if is_valid.get(val, 0) > 0:
                        is_valid[val] -= 1
                        if is_valid[val] == 0:
                            del is_valid[val]
                        break

    # 최댓값, 최솟값 구하기
    if not is_valid:
        print("EMPTY")
    else:
        # min_heap에서 유효한 최솟값 찾기
        min_val = None
        while min_heap:
            val = heapq.heappop(min_heap)
            if is_valid.get(val, 0) > 0:
                min_val = val
                # 다시 유효하므로 개수 유지 위해 push하고 break
                heapq.heappush(min_heap, val)
                break

        # max_heap에서 유효한 최댓값 찾기
        max_val = None
        while max_heap:
            val = -heapq.heappop(max_heap)
            if is_valid.get(val, 0) > 0:
                max_val = val
                heapq.heappush(max_heap, -val)
                break

        print(max_val, min_val)
