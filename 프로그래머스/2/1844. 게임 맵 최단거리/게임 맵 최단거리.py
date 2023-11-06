from collections import deque

def solution(maps):
    dx = [1,-1, 0, 0] # X 방향의 움직임, dx[0]은 X방향으로 1(->) dx[1]은 X방향으로 -1 (<-)
    dy = [0, 0, 1, -1] 

    # map의 크기
    n  = len(maps)
    m = len(maps[0])

    # 큐
    queue = deque()
    queue.append((0, 0))

    # queue가 빌 때까지 (즉 모든 곳을 방문) 할 때까지 반복
    while queue:
        # 현재위치 로딩
        x, y = queue.popleft()

        # for 문으로 현재 위치에서 상하좌우 다 찔러봄
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 현재위치에서 상하좌우 좌표가 갈수 있는지 확인
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # 만약 갈 수 있으면 현재 스텝의 +1 해서 몇 번만에 방문했는지 기록
                maps[nx][ny] = maps[x][y]+1
                # 그리고 다음에 현재위치로 쓰기위해 큐에 넣음
                queue.append((nx, ny))

    answer = maps[n-1][m-1]

    if answer == 1:
        answer = -1

    return answer