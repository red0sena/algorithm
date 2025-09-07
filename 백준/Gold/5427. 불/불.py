import sys
from collections import deque

# 빠른 입력을 위한 설정
input = sys.stdin.readline

# 동서남북 이동 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solve():
    """
    하나의 테스트 케이스를 해결하는 함수
    """
    w, h = map(int, input().split())
    # 지도 정보 입력 받기
    board = [list(input().strip()) for _ in range(h)]

    # 불과 상근이의 위치를 저장할 큐
    fire_q = deque()
    person_q = deque()

    # 방문 여부 및 불의 확산 시간을 저장할 배열
    # -1은 아직 방문/도달하지 않았음을 의미
    fire_dist = [[-1] * w for _ in range(h)]
    person_dist = [[-1] * w for _ in range(h)]

    # 초기 위치 설정
    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                person_q.append((i, j))
                person_dist[i][j] = 0
            elif board[i][j] == '*':
                fire_q.append((i, j))
                fire_dist[i][j] = 0

    # 1. 불의 확산 시간 계산 (Fire BFS)
    while fire_q:
        x, y = fire_q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 지도 범위 내에 있고, 벽이 아니며, 아직 불이 붙지 않은 곳
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] != '#' and fire_dist[nx][ny] == -1:
                    fire_dist[nx][ny] = fire_dist[x][y] + 1
                    fire_q.append((nx, ny))

    # 2. 상근이의 탈출 경로 탐색 (Sang-geun BFS)
    while person_q:
        x, y = person_q.popleft()

        # 현재 위치에서 탈출 가능한지 확인
        if x == 0 or x == h - 1 or y == 0 or y == w - 1:
            print(person_dist[x][y] + 1)
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 지도 범위 내에 있고
            if 0 <= nx < h and 0 <= ny < w:
                # 빈 공간이며, 아직 방문하지 않았고
                if board[nx][ny] == '.' and person_dist[nx][ny] == -1:
                    # 불이 아직 도달하지 않았거나, 상근이가 불보다 먼저 도착하는 경우
                    if fire_dist[nx][ny] == -1 or person_dist[x][y] + 1 < fire_dist[nx][ny]:
                        person_dist[nx][ny] = person_dist[x][y] + 1
                        person_q.append((nx, ny))
                        # 다음 위치가 탈출구인 경우 즉시 결과 출력
                        if nx == 0 or nx == h - 1 or ny == 0 or ny == w - 1:
                            print(person_dist[nx][ny] + 1)
                            return
    
    # 큐가 비었는데 탈출하지 못한 경우
    print("IMPOSSIBLE")

# 테스트 케이스의 수만큼 반복
T = int(input())
for _ in range(T):
    solve()