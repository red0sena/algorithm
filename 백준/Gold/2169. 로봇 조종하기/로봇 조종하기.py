import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j]: i번째 행, j번째 열에 도달했을 때 얻을 수 있는 최대 점수
dp = [[0]*M for _ in range(N)]
dp[0][0] = grid[0][0]

# 첫 번째 행은 왼쪽에서 오른쪽으로만 누적
for j in range(1, M):
    dp[0][j] = dp[0][j-1] + grid[0][j]

# 2번째 행부터 N-1번째 행까지 처리
for i in range(1, N):
    # 왼쪽에서 오른쪽으로 누적할 임시 배열
    leftToRight = [0]*M
    leftToRight[0] = dp[i-1][0] + grid[i][0]
    for j in range(1, M):
        # 위에서 내려온 값(dp[i-1][j]) 혹은 왼쪽에서 온 값(leftToRight[j-1]) 중 더 큰 값을 사용
        leftToRight[j] = max(dp[i-1][j], leftToRight[j-1]) + grid[i][j]

    # 오른쪽에서 왼쪽으로 누적할 임시 배열
    rightToLeft = [0]*M
    rightToLeft[M-1] = dp[i-1][M-1] + grid[i][M-1]
    for j in range(M-2, -1, -1):
        # 위에서 내려온 값(dp[i-1][j]) 혹은 오른쪽에서 온 값(rightToLeft[j+1]) 중 더 큰 값을 사용
        rightToLeft[j] = max(dp[i-1][j], rightToLeft[j+1]) + grid[i][j]

    # 현재 행의 최종 dp 값은 두 방향에서 구한 값 중 최댓값
    for j in range(M):
        dp[i][j] = max(leftToRight[j], rightToLeft[j])

print(dp[N-1][M-1])
