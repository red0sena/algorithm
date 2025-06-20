import sys
input = sys.stdin.readline

# 방향 벡터 (1~8)
# 1: ←, 2: ↖, 3: ↑, 4: ↗, 5: →, 6: ↘, 7: ↓, 8: ↙
dr = [0,  0, -1, -1, -1,  0,  1,  1,  1]
dc = [0, -1, -1,  0,  1,  1,  1,  0, -1]

# 대각선 4방향 (물복사 버그용)
diag = [(-1,-1), (-1,1), (1,-1), (1,1)]

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
commands = [tuple(map(int, input().split())) for _ in range(M)]

# 초기 구름 위치 (0-indexing)
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for d, s in commands:
    # 1) 구름 이동 & 비 내리기
    new_clouds = []
    for r, c in clouds:
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        new_clouds.append((nr, nc))
        A[nr][nc] += 1

    # 2) 물복사 버그
    for r, c in new_clouds:
        cnt = 0
        for drd, dcd in diag:
            rr, cc = r + drd, c + dcd
            if 0 <= rr < N and 0 <= cc < N and A[rr][cc] > 0:
                cnt += 1
        A[r][c] += cnt

    # 3) 구름 소멸 → 물의 양이 2 이상인 곳에 새 구름 생성
    prev = set(new_clouds)
    clouds = []
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and (i, j) not in prev:
                clouds.append((i, j))
                A[i][j] -= 2

# 결과: 모든 칸의 물의 양 합
answer = sum(map(sum, A))
print(answer)
