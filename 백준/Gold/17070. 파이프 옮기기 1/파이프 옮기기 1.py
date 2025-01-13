n = int(input())
input_map = [list(map(int, input().split(' '))) for _ in range(n)]

# 3차원 visited 배열: visited[x][y][direction]
# direction: 0(가로), 1(대각), 2(세로)
visited = [[[-1] * 3 for _ in range(n)] for _ in range(n)]


move_1 = [(0,1),(1,1)]
move_2 = [(0,1),(1,1),(1,0)]
move_3 = [(1,0), (1,1)]




def dfs(x, y, bdx, bdy):
    # (N-1, N-1)에 도달한 경우 -> 방법 1개 카운트
    if x == n - 1 and y == n - 1:
        return 1

    if bdx == 0 and bdy == 1:
        move = move_1
        direction = 0
    elif bdx == 1 and bdy == 1:
        move = move_2
        direction = 1
    elif bdx == 1 and bdy == 0:
        move = move_3
        direction = 2


    if visited[x][y][direction] != -1:
        return visited[x][y][direction]

    val = 0


    # 각 후보 위치(nx, ny)로 이동할 수 있는지 검사 후, 재귀 호출
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        # 좌표 범위 확인
        if 0 <= nx < n and 0 <= ny < n:
            if dx == 1 and dy == 1:
                if any([input_map[x+1][y], input_map[x+1][y+1], input_map[x][y+1]]):
                    continue
            else:
                if input_map[nx][ny] == 1:
                    continue

            val += dfs(nx, ny, dx, dy)

    visited[x][y][direction] = val
    return val

answer = dfs(0, 1, 0, 1)

print(answer)
