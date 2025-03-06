from itertools import permutations
import copy
n, m = map(int, input().split())
input_list = [list(map(int, input().split())) for _ in range(n)]

# 1. 모든 CCTV좌표를 가져옴
# 2. 상하좌우 CCTV를 돌린 후 가장 많은 부분을 감시할 수 있는 방향 count
# 3. 한번 count된 방향은 방문 처리하여 나중에 count하지 않도록 함


move = [(1,0),(0,1),(-1,0),(0,-1)]

# 0 우
# 1 하
# 2 좌
# 3 상

cctv_direction = [
    [None],
    [[(0, 1)], [(1, 0)], [(0, -1)], [(-1,0)]], # 한 방향

    [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]], # 두 방향 수평

    [[(0, 1), (-1, 0)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)]], # 두 방향 직각

    [[(0, 1), (0, -1), (-1, 0)], [(0, 1), (-1, 0), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],  # 세 방향

    [[(0, 1), (1, 0), (-1, 0), (0, -1)]] # 네 방향

]
def all_combi(combi):
    global cctv_xy
    tmp_input_list = copy.deepcopy(input_list)

    def look_forward(cctv_num, x, y):
        max_count = -int(10e10)
        all_direction = cctv_direction[cctv_num]
        for direction in all_direction:
            count = 0
            for dx, dy in direction:
                nx = x
                ny = y
                while True:
                    nx += dx
                    ny += dy
                    if 0 > nx or nx >= n or 0 > ny or ny >= m:
                        break
                    else:
                        if tmp_input_list[nx][ny] == 6:
                            break
                        elif tmp_input_list[nx][ny] == 0:
                            count += 1

            max_count = max(count, max_count)
            if count == max_count:
                max_direction = direction
        for dx, dy in max_direction:
            nx = x
            ny = y
            while True:
                nx += dx
                ny += dy
                if 0 > nx or nx >= n or 0 > ny or ny >= m:
                    break
                else:
                    if tmp_input_list[nx][ny] == 6:
                        break
                    elif tmp_input_list[nx][ny] == 0:
                        tmp_input_list[nx][ny] = -1

    for a in combi:
        i, j = cctv_xy[a]
        look_forward(tmp_input_list[i][j], i, j)

    res = 0
    for i in range(n):
        for j in range(m):
            if tmp_input_list[i][j] == 0:
                res += 1

    return res
cctv_xy = []

for i in range(n):
    for j in range(m):
        if input_list[i][j] in [1,2,3,4,5]:
            cctv_xy.append((i, j))

xy_combi = list(permutations(range(0, len(cctv_xy)), len(cctv_xy)))
res = int(10e10)

for combi in xy_combi:
    res = min(res, all_combi(combi))
print(res)

