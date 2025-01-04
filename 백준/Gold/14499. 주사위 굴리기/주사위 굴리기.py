# 1 동
# 2 서
# 3 북
# 4 남
n, m, x, y, k = map(int, input().split(' '))
input_arr = [list(map(int, input().split())) for _ in range(n)]
command_list = list(map(int, input().split()))
move_command = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
dice_map = [0,0,0,0,0,0]
# 0동, 1서, 2남, 3북, 4위, 5아래

for command in command_list:
    mx, my = move_command[command]
    # print(x + mx, y + my)
    if x + mx >= n or y + my >= m or y + my < 0 or x + mx < 0:
        continue

    x = x + mx
    y = y + my
    # print(command)
    dice_map_copy = dice_map.copy()
    if command == 1:
        dice_map[1] = dice_map_copy[5]
        dice_map[0] = dice_map_copy[4]
        # 북남은 제외
        # dice_map[2] = dice_map_copy[5]
        # dice_map[3] = dice_map_copy[5]
        dice_map[4] = dice_map_copy[1]
        dice_map[5] = dice_map_copy[0]
    elif command == 2:
        dice_map[0] = dice_map_copy[5]
        dice_map[1] = dice_map_copy[4]
        # 북남은 제외
        # dice_map[2] = dice_map_copy[5]
        # dice_map[3] = dice_map_copy[5]
        dice_map[4] = dice_map_copy[0]
        dice_map[5] = dice_map_copy[1]
    elif command == 3: # 0동, 1서, 2남, 3북, 4위, 5아래
        # dice_map[0] = dice_map_copy[5]
        # dice_map[1] = dice_map_copy[4]
        dice_map[2] = dice_map_copy[5]
        dice_map[3] = dice_map_copy[4]
        dice_map[4] = dice_map_copy[2]
        dice_map[5] = dice_map_copy[3]
    elif command == 4:
        # dice_map[0] = dice_map_copy[5]
        # dice_map[1] = dice_map_copy[4]
        dice_map[2] = dice_map_copy[4]
        dice_map[3] = dice_map_copy[5]
        dice_map[4] = dice_map_copy[3]
        dice_map[5] = dice_map_copy[2]

    if input_arr[x][y] == 0:
        input_arr[x][y] = dice_map[5]
    else:
        dice_map[5] = input_arr[x][y]
        input_arr[x][y] = 0

    print(dice_map[4])
    # print('동', dice_map[0])
    # print('서', dice_map[1])
    # print('남', dice_map[2])
    # print('북', dice_map[3])
    # print('위', dice_map[4])
    # print('아래', dice_map[5])
