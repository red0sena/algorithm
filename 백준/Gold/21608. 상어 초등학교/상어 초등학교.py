
n = int(input())

class_room = [[0] * n for _ in range(n)]

# 인접은 현재 위치에서 상하좌우
move = [(0,1), (1,0), (0,-1), (-1,0)]



def find_suki_friend_seat(num, suki_student_list):
    friend_seat = []
    max_count = 0
    max_friend_seat_xy = set()
    for i in range(n):
        for j in range(n):
            if class_room[i][j] == 0:
                count = 0
                for dx, dy in move:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if class_room[nx][ny] in suki_student_list:
                            count += 1
                if count == max_count:
                    friend_seat.append((i, j))
                elif count > max_count:
                    friend_seat.clear()
                    max_count = count
                    friend_seat.append((i, j))

    if len(friend_seat) == 1:
        i, j = friend_seat[0]
        class_room[i][j] = num
        return []
    return friend_seat



def find_empty_seat(num, seat_list):
    friend_seat = []
    max_count = 0
    for i, j in seat_list:
        count = 0
        for dx, dy in move:
            nx = i + dx
            ny = j + dy
            if 0 <= nx < n and 0 <= ny < n:
                if class_room[nx][ny] == 0:
                    count += 1
        if count == max_count:
            friend_seat.append((i, j))
        elif count > max_count:
            friend_seat.clear()
            max_count = count
            friend_seat.append((i, j))

    if len(friend_seat) == 1:
        i, j = friend_seat[0]
        class_room[i][j] = num
        return []
    return friend_seat
def find_min_row_col_seat(num, seat_list):
    seat_list = sorted(seat_list, key=lambda x:(x[0], x[1]))
    i,j = seat_list[0]
    class_room[i][j] = num

kv_dict = {}
for _ in range(n*n):
    student_num, stdent_suki1, stdent_suki2, stdent_suki3, stdent_suki4 = map(int, input().split())
    kv_dict[student_num] = [stdent_suki1, stdent_suki2, stdent_suki3, stdent_suki4]
    v1 = find_suki_friend_seat(student_num, [stdent_suki1, stdent_suki2, stdent_suki3, stdent_suki4]) # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    if v1:
        v2 = find_empty_seat(student_num, v1) #  인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.\
        if v2:
            find_min_row_col_seat(student_num, v2) # 행렬의 번호가 가장 작은 칸

res = 0

for i in range(n):
    for j in range(n):
        student_num = class_room[i][j]
        suki_list = kv_dict[student_num]
        count = 0
        for dx, dy in move:
            nx = i + dx
            ny = j + dy
            if 0 <= nx < n and 0 <= ny < n:
                if class_room[nx][ny] in suki_list:
                    count += 1


        if count == 1:
            res += 1
        elif count == 2:
            res += 10
        elif count == 3:
            res += 100
        elif count == 4:
            res += 1000


print(res)