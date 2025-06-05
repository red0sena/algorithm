import sys
input = sys.stdin.readline

# 입력 처리
N = int(input())
solutions = list(map(int, input().split()))

# 투 포인터 초기화
left, right = 0, N - 1
min_diff = float('inf')  # 0과의 최소 차이
answer = [0, 0]  # 결과 용액 쌍

# 투 포인터로 탐색
while left < right:
    current_sum = solutions[left] + solutions[right]
    current_diff = abs(current_sum)
    
    # 최소 차이 갱신
    if current_diff < min_diff:
        min_diff = current_diff
        answer = [solutions[left], solutions[right]]
    
    # 합이 0에 가까워지도록 포인터 이동
    if current_sum < 0:
        left += 1
    elif current_sum > 0:
        right -= 1
    else:
        # 합이 0이면 최적 해이므로 종료
        break

# 결과 출력 (오름차순)
print(answer[0], answer[1])