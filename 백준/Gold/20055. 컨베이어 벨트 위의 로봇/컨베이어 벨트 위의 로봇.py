from collections import deque




n, k = map(int, input().split())

input_list = list(map(int, input().split()))

conveyor_belt = deque(input_list)

robot_list = []


# 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
# 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    # 2-1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
# 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.

time_sec = 0
while True:

    # 1.
    pop_v = conveyor_belt.pop()
    conveyor_belt.appendleft(pop_v)
    for i in range(len(robot_list)):
        robot_list[i] += 1

    if len(robot_list) > 0:
        if robot_list[0] == n-1:
            robot_list = robot_list[1:]

    # 2.
    for i in range(len(robot_list)):
        idx = robot_list[i]
        if idx + 1 not in robot_list: # 이동하려는 칸에 로봇이 없으며
            if conveyor_belt[idx+1] > 0: # 그 칸의 내구도가 1 이상이어야 한다.
                robot_list[i] = idx + 1
                conveyor_belt[idx+1] -= 1
    if len(robot_list) > 0:
        if robot_list[0] == n-1:
            robot_list = robot_list[1:]



    # 3.
    if conveyor_belt[0] != 0: #  올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
        robot_list.append(0)
        conveyor_belt[0] -= 1


    time_sec += 1
    if conveyor_belt.count(0) >= k: # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
        print(time_sec)
        break

