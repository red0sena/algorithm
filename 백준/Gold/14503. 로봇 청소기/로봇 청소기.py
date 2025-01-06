n, m = map(int, input().split(" "))
r, c, d = map(int, input().split(" "))

room_map = [list(map(int, input().split(" "))) for _ in range(n)]
# 0:북, 1:동, 2:남, 3:서
move = [(-1,0), (0,1), (1,0), (0,-1)]


res = 0

while True:
    if room_map[r][c] == 0:
        room_map[r][c] = 2
        res += 1
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    if (room_map[r-1][c] == 0) or (room_map[r][c-1] == 0) or (room_map[r+1][c] == 0) or (room_map[r][c+1] == 0):
        for _ in range(4):
            # 반시계 방향으로 90도 회전한다.
            d -= 1
            if d < 0:
                d = 3
            dx, dy = move[d]
            nx, ny = r+dx, c+dy
            if room_map[nx][ny] == 0:
                r, c = nx, ny
                break

    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    elif (room_map[r-1][c] != 0) and (room_map[r][c-1] != 0) and (room_map[r+1][c] != 0) and (room_map[r][c+1] != 0):
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        back_d = d + 2
        if back_d > 3:
            back_d -= 4
        bx, by = move[back_d]
        nx, ny = r + bx, c + by

        if room_map[nx][ny] == 1:
            print(res)
            exit()
        else:
            # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            r, c = nx, ny

