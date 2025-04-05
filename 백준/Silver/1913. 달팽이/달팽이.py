n = int(input())
find_num = int(input())
arr = [[0] * n for _ in range(n)]


find_num_xy = tuple()

def tornado():
    global arr
    global find_num_xy
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    y = len(arr) // 2
    x = len(arr) // 2
    num = 1  # 칸에 채워넣을 값
    dist = 1
    d_idx = 0  # 서 남 동 북 순서
    move_count = 0  # 2가 되면 dist 길이가 1 늘어나고 move_count는 다시 0으로 초기화
    arr[x][y] = 1
    while True:
        for _ in range(dist):
            dx, dy = d[d_idx]
            ny = dy + y
            nx = dx + x
            if (nx, ny) == (-1, 0): # 토네이도가 끝날 때 좌표
                return
            num += 1
            if num == find_num:
                find_num_xy = (nx, ny)
            arr[nx][ny] = num
            y = ny
            x = nx
        move_count += 1
        d_idx = (d_idx + 1) % 4
        if move_count == 2:
            dist += 1
            move_count = 0


tornado()
for i in range(n):
    print(*arr[i])
if find_num_xy:
    print(find_num_xy[0]+1, find_num_xy[1]+1)
else:
    print(n // 2 + 1, n // 2 + 1)