# 입력 처리
N, K = map(int, input().split())
houses = []
for _ in range(N):
    x, y = map(int, input().split())
    houses.append((x, y))

# 모든 집 쌍 간의 맨해튼 거리 계산
dist = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        dist[i][j] = abs(houses[i][0] - houses[j][0]) + abs(houses[i][1] - houses[j][1])

# K에 따라 최대 거리를 최소화하는 함수
def solve():
    global N, K, dist
    min_max_dist = float('inf')

    if K == 1:
        # K=1: 각 집을 대피소로 선택했을 때 최대 거리 계산
        for i in range(N):
            max_dist = 0
            for j in range(N):
                max_dist = max(max_dist, dist[j][i])
            min_max_dist = min(min_max_dist, max_dist)

    elif K == 2:
        # K=2: 모든 두 집 쌍을 대피소로 선택
        for i in range(N):
            for j in range(i + 1, N):
                max_dist = 0
                for k in range(N):
                    min_to_shelter = min(dist[k][i], dist[k][j])
                    max_dist = max(max_dist, min_to_shelter)
                min_max_dist = min(min_max_dist, max_dist)

    elif K == 3:
        # K=3: 모든 세 집 조합을 대피소로 선택
        for i in range(N):
            for j in range(i + 1, N):
                for m in range(j + 1, N):
                    max_dist = 0
                    for k in range(N):
                        min_to_shelter = min(dist[k][i], dist[k][j], dist[k][m])
                        max_dist = max(max_dist, min_to_shelter)
                    min_max_dist = min(min_max_dist, max_dist)

    return min_max_dist

# 결과 출력
print(solve())