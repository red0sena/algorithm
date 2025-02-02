import sys
input = sys.stdin.readline

# 1) N, K 입력 받기
N, K = map(int, input().split())
# 2) 온도 리스트 입력 받기
temps = list(map(int, input().split()))

# 3) 처음 K개의 합을 구함
current_sum = sum(temps[:K])
max_sum = current_sum

# 4) 슬라이딩 윈도우(투 포인터)로 최댓값 찾기
#    i는 오른쪽 포인터를 의미, i가 한 칸씩 오른쪽으로 이동
for i in range(K, N):
    # 윈도우에서 빠져나가는 값 빼고, 새로 들어오는 값 더하기
    current_sum = current_sum - temps[i-K] + temps[i]
    # 최대합 갱신
    if current_sum > max_sum:
        max_sum = current_sum

# 5) 결과 출력
print(max_sum)