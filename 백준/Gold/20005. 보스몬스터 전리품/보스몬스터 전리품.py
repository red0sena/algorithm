from collections import deque
n, m, p = map(int, input().split())

input_list = [list(input()) for _ in range(n)]

player_dps = {}
for _ in range(p):
    player_id, dps = input().split()
    player_dps[player_id] = int(dps)

monster_hp = int(input())

player_xy = []
for i in range(n):
    for j in range(m):
        if input_list[i][j] != '.' and input_list[i][j] != 'X' and input_list[i][j] != 'B':
            player_xy.append((i,j))

def bfs(sx,sy):
    visited = [[-1] * m for _ in range(n)]
    move = [(0,1),(1,0),(-1,0),(0,-1)]
    q = deque([(sx,sy,0)])
    visited[sx][sy] = 1

    while q:
        x, y, time = q.popleft()
        if input_list[x][y] == 'B':
            return time
        for dx, dy in move:
            nx = dx + x
            ny = dy + y
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1 and input_list[nx][ny] != 'X':
                    visited[nx][ny] = 1
                    q.append((nx,ny,time+1))


    return -1

player_takes_time = {}
player_count = {}
for px, py in player_xy:
    p_id = input_list[px][py]
    takes_time = bfs(px, py)
    player_takes_time[takes_time] = player_takes_time.get(takes_time, 0) + player_dps[p_id]
    player_count[takes_time] = player_count.get(takes_time, 0) + 1


player_takes_time = dict(sorted(player_takes_time.items()))
before_time = 0
res = 0
i = list(player_takes_time.keys())[0]
total_dps = 0
while True:
    if i in player_takes_time:
        total_dps += player_takes_time[i]
        monster_hp -= total_dps
        res += player_count[i]
    else:
        monster_hp -= total_dps
    if monster_hp <= 0:
        print(res)
        break
    i += 1


# 각 플레이어가 보스에 도착할 수 있는 최단시간을 구한다.
# 가장 빨리 도착한애 부터 점차 보스 피를 깍아나가기 시작함
# 보스 피가 0이 되는 초를 구한 후 그 초보다 빨리 도착한 플레이어를 count해서 출력한다.