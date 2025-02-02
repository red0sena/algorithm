import sys

input = sys.stdin.readline
# 입력 받기
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 투 포인터를 이용한 풀이
start, end = 0, 0
current_sum = 0
answer = float('inf')

while True:
    # 현재 합이 S 미만이고, end가 범위 안에 있다면
    if current_sum < S and end < N:
        current_sum += arr[end]
        end += 1
    # 현재 합이 S 이상이면 최솟값 갱신 후 start를 이동
    elif current_sum >= S:
        answer = min(answer, end - start)
        current_sum -= arr[start]
        start += 1
    else:
        # 더 이상 탐색할 수 없는 경우 종료
        break

# 만약 갱신되지 않았다면 0 출력, 그렇지 않다면 answer 출력
print(0 if answer == float('inf') else answer)
