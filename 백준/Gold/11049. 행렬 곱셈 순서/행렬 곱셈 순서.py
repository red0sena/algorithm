import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
DP = [[0]*N for _ in range(N)]

# 분할된 그룹의 크기를 1부터 N-1까지 돎
for size in range(1, N):
	# 크기 size인 그룹의 모든 경우의 수 돎
    for start in range(N - size):
        end = start + size
        
        # 어떤 그룹의 최소 곱셈 횟수는 분할한 두 그룹의 최소 곱셈 횟수 + 각 그룹의 곱셈 다 끝나고 남은 행렬끼리의 곱셈 횟수
        result = float("inf")
        for cut in range(start, end):
            result = min(result, DP[start][cut] + DP[cut+1][end] +
                        matrix[start][0]*matrix[cut][1]*matrix[end][1])
        DP[start][end] = result

print(DP[0][-1])